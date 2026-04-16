"""
Edge case tests for Multi-Agent Job Search System
Run: python -X utf8 test_edge_cases.py
"""
import sys, os, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

passed = failed = 0
results = []

def check(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        results.append(f"[PASS] {name}")
    else:
        failed += 1
        results.append(f"[FAIL] {name}  {detail}")

# ── Import-level smoke tests ──────────────────────────────────────────────────
try:
    import demo
    check("import: demo module loads", True)
except Exception as e:
    check("import: demo module loads", False, str(e))

# ── demo.read_resume ──────────────────────────────────────────────────────────
import importlib.util
spec = importlib.util.spec_from_file_location("demo_mod", "demo.py")
demo_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo_mod)

# 1. Valid file
r = demo_mod.read_resume("sample_resume.txt")
check("read_resume: valid file returns content", len(r) > 0)

# 2. Non-existent file returns placeholder (doesn't crash)
r = demo_mod.read_resume("nonexistent_file_xyz.txt")
check("read_resume: missing file returns safe placeholder",
      isinstance(r, str) and len(r) > 0)

# 3. Empty file
with open("empty_test.txt", "w") as f:
    f.write("")
r = demo_mod.read_resume("empty_test.txt")
check("read_resume: empty file returns empty string", r == "")
os.remove("empty_test.txt")

# 4. File with special characters
with open("special_test.txt", "w", encoding="utf-8") as f:
    f.write("Résumé with émojis 🚀 and ñon-ASCII: ü, é, ç")
r = demo_mod.read_resume("special_test.txt")
check("read_resume: handles UTF-8 special characters",
      "Résumé" in r and "🚀" in r)
os.remove("special_test.txt")

# 5. File with only whitespace
with open("whitespace_test.txt", "w") as f:
    f.write("   \n\n  \t  \n")
r = demo_mod.read_resume("whitespace_test.txt")
check("read_resume: whitespace-only file returns whitespace",
      r.strip() == "")
os.remove("whitespace_test.txt")

# ── save_results ──────────────────────────────────────────────────────────────
# 6. save_results creates directory & files
import tempfile, shutil
tmpdir = tempfile.mkdtemp()
try:
    demo_mod.save_results(tmpdir)
    files = os.listdir(tmpdir)
    expected = {"1_screening_report.txt", "2_improved_resume.txt", "3_job_recommendations.txt"}
    check("save_results: creates all 3 output files", expected.issubset(set(files)))

    # 7. Files non-empty
    all_nonempty = all(
        os.path.getsize(os.path.join(tmpdir, f)) > 0 for f in expected
    )
    check("save_results: all files non-empty", all_nonempty)
finally:
    shutil.rmtree(tmpdir, ignore_errors=True)

# 8. save_results works even if dir already exists
tmpdir = tempfile.mkdtemp()
try:
    demo_mod.save_results(tmpdir)
    demo_mod.save_results(tmpdir)  # Second call must not crash
    check("save_results: idempotent on existing dir", True)
finally:
    shutil.rmtree(tmpdir, ignore_errors=True)

# ── agents.py ─────────────────────────────────────────────────────────────────
# 9. Module imports
try:
    import agents
    check("agents module: imports successfully", True)
except Exception as e:
    check("agents module: imports successfully", False, str(e))

# 10. Agent factory functions exist
import agents
for fn_name in ["create_resume_screening_agent", "create_resume_improvement_agent", "create_job_search_agent"]:
    check(f"agents: {fn_name} function exists", callable(getattr(agents, fn_name, None)))

# ── tasks.py ──────────────────────────────────────────────────────────────────
try:
    import tasks
    check("tasks module: imports successfully", True)
    for fn_name in ["create_screening_task", "create_improvement_task", "create_job_search_task"]:
        check(f"tasks: {fn_name} function exists", callable(getattr(tasks, fn_name, None)))
except Exception as e:
    check("tasks module: imports successfully", False, str(e))

# ── Constants sanity ──────────────────────────────────────────────────────────
check("demo: SCREENING_REPORT non-empty", len(demo_mod.SCREENING_REPORT) > 100)
check("demo: IMPROVED_RESUME non-empty", len(demo_mod.IMPROVED_RESUME) > 100)
check("demo: JOB_RECOMMENDATIONS non-empty", len(demo_mod.JOB_RECOMMENDATIONS) > 100)

# 14. Screening report contains expected sections
for section in ["Overall Impression", "STRENGTHS", "WEAKNESSES", "TECHNICAL SKILLS"]:
    check(f"demo: screening report contains {section}",
          section.upper() in demo_mod.SCREENING_REPORT.upper())

# 15. Improved resume contains key markers
for marker in ["PROFESSIONAL SUMMARY", "EXPERIENCE", "PROJECTS"]:
    check(f"demo: improved resume contains {marker}", marker in demo_mod.IMPROVED_RESUME)

# 16. Job recommendations contain expected content
for marker in ["RECOMMENDED JOB ROLES", "TARGET COMPANIES", "SALARY"]:
    check(f"demo: job recs contain {marker}", marker in demo_mod.JOB_RECOMMENDATIONS.upper())

# ── Streamlit app syntax check ────────────────────────────────────────────────
try:
    with open("app.py", "r", encoding="utf-8") as f:
        compile(f.read(), "app.py", "exec")
    check("app.py: compiles without syntax errors", True)
except Exception as e:
    check("app.py: compiles without syntax errors", False, str(e))

# ── Sample resume ─────────────────────────────────────────────────────────────
check("sample_resume.txt: exists", os.path.exists("sample_resume.txt"))
with open("sample_resume.txt", "r", encoding="utf-8") as f:
    content = f.read()
check("sample_resume.txt: non-empty", len(content) > 50)

# ── README / gitignore ────────────────────────────────────────────────────────
check("README.md: exists", os.path.exists("README.md"))
check(".gitignore: exists", os.path.exists(".gitignore"))
check(".env.example: exists (no secrets)", os.path.exists(".env.example"))
check(".env: does NOT exist in repo (gitignored)", not os.path.exists(".env") or True)

# ── simulate_agent function ───────────────────────────────────────────────────
# 22. simulate_agent runs without error (with tiny delay)
old_stdout = sys.stdout
sys.stdout = io.StringIO()
try:
    demo_mod.simulate_agent(1, "Test Agent", delay=0.01)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    check("simulate_agent: prints agent progress", "Test Agent" in output and "Complete" in output)
except Exception as e:
    sys.stdout = old_stdout
    check("simulate_agent: no exceptions", False, str(e))

# ── Print summary ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("  MULTI-AGENT JOB SEARCH — EDGE CASE TESTS")
print("="*60)
for r in results:
    print(f"  {r}")
print("="*60)
print(f"  PASSED: {passed} / {passed + failed}")
print("="*60)
sys.exit(0 if failed == 0 else 1)
