#!/usr/bin/env python3
"""Refresh the LLM-advertising repo index from the GitHub API.

v2 additions:
  - days-since-last-push column
  - per-repo KIND (code / spec / list / research) so umbrella & schema repos
    are not falsely flagged "stale" (they are expected to be low-churn)
  - kind-aware freshness verdict
  - per-family + per-kind activity summary
  - graceful 403 / rate-limit handling with token hint

Unauthenticated GitHub API = 60 req/hr (this index has 18 repos). For reliable,
repeatable runs, set a token:  GITHUB_TOKEN=<token> python3 refresh_repo_index.py
"""
import json, os, sys, urllib.request, urllib.error
from datetime import datetime, timezone

STALE_DAYS = 90       # code/list: warn if no push in this many days
DORMANT_DAYS = 365    # research: mark long-dormant

# repo -> (family, kind, last_recorded_stars)
# kind: code=active software | spec=umbrella/schema (low churn OK)
#       list=curated list | research=academic prototype (dormancy expected)
REPOS = {
 "adcontextprotocol/adcp":                      ("A", "code",     240),
 "IABTechLab/agentic-audiences":                ("A", "code",     41),
 "IABTechLab/agentic-real-time-framework":      ("A", "code",     24),
 "IABTechLab/seller-agent":                     ("A", "code",     23),
 "IABTechLab/buyer-agent":                      ("A", "code",     23),
 "IABTechLab/AAMP":                             ("A", "spec",     18),
 "adcontextprotocol/adcp-client":               ("A", "code",     18),
 "IABTechLab/agentic-direct":                   ("A", "spec",     8),
 "jshorwitz/awesome-agentic-advertising":       ("B", "list",     33),
 "itallstartedwithaidea/advertising-hub":       ("B", "code",     31),
 "itallstartedwithaidea/agent-skills":          ("B", "code",     31),
 "fseixas/chatgpt-ads-builder":                 ("B", "code",     7),
 "PaidSync/paidsync-mcp":                       ("B", "code",     1),
 "pxpilot/adcp-sandbox":                        ("B", "code",     0),
 "chaovven/maab":                               ("C", "research", 27),
 "lab1806/LLM-advertising-fusion":              ("C", "research", 5),
 "MuzhiMa/Quality-Preserving_LLM_Advertising":  ("C", "research", 0),
 "DevPranjal/steroiADs":                        ("C", "research", 1),
}


def days_since(pushed_iso, today=None):
    """Whole days between an ISO date (YYYY-MM-DD...) and today (UTC)."""
    if not pushed_iso:
        return None
    today = today or datetime.now(timezone.utc)
    d = datetime.strptime(pushed_iso[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return (today - d).days


def verdict(kind, age):
    """Kind-aware freshness label. Returns (label, is_concern)."""
    if age is None:
        return ("?", False)
    if kind == "spec":
        return ("umbrella/spec (churn N/A)", False)
    if kind == "research":
        if age > DORMANT_DAYS:
            return (f"dormant {age}d (expected for research)", False)
        if age > STALE_DAYS:
            return (f"quiet {age}d", False)
        return (f"active {age}d", False)
    # code / list
    if age > STALE_DAYS:
        return (f"STALE {age}d", True)
    return (f"fresh {age}d", False)


def fetch(repo, today=None):
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(
        url, headers={"Accept": "application/vnd.github+json", "User-Agent": "atlas-refresh"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
        pushed = (d.get("pushed_at") or "")[:10]
        age = days_since(pushed, today)
        return {"status": "ok", "stars": d.get("stargazers_count"),
                "lang": d.get("language"), "pushed": pushed, "age": age,
                "archived": d.get("archived")}
    except urllib.error.HTTPError as e:
        hint = "  (rate limit — set GITHUB_TOKEN)" if e.code == 403 else ""
        return {"status": f"HTTP {e.code}{hint}"}
    except Exception as e:
        return {"status": f"ERR {e}"}


def main():
    today = datetime.now(timezone.utc)
    print(f"# Repo index refresh — {today:%Y-%m-%d}\n")
    print("| Fam | Kind | Repo | ★now | ★was | Δ | Lang | Last push | Age | Freshness |")
    print("|---|---|---|---:|---:|---:|---|---|---:|---|")
    summary = {}
    concerns, renamed = [], []
    for repo, (fam, kind, old) in REPOS.items():
        info = fetch(repo, today)
        summary.setdefault(fam, {"n": 0, "concern": 0})
        summary[fam]["n"] += 1
        if info["status"] != "ok":
            print(f"| {fam} | {kind} | {repo} | — | {old} | — | — | — | — | **{info['status']}** |")
            if "404" in info["status"]:
                renamed.append(repo)
            continue
        now = info["stars"]; delta = now - old
        lab, concern = verdict(kind, info["age"])
        arch = " archived" if info.get("archived") else ""
        if concern:
            summary[fam]["concern"] += 1
            concerns.append(f"{repo} ({info['age']}d)")
        age = "-" if info["age"] is None else str(info["age"])
        print(f"| {fam} | {kind} | {repo} | {now} | {old} | {delta:+d} | "
              f"{info['lang']} | {info['pushed']}{arch} | {age} | {lab} |")

    print("\n## Summary")
    for fam in sorted(summary):
        s = summary[fam]
        print(f"- Family {fam}: {s['n']} repos, {s['concern']} stale-concern "
              f"(code/list not pushed in {STALE_DAYS}d).")
    print(f"- Stale-concern repos: {', '.join(concerns) if concerns else 'none'}")
    if renamed:
        print(f"- Renamed/deleted (404): {', '.join(renamed)}")
    print("- Note: 'spec' (umbrella/schema) and 'research' repos are not treated "
          "as stale on push-age alone.")


if __name__ == "__main__":
    main()
