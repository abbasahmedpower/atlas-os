"""Deterministic structural checks for V4 artifact; NOT evaluation of an AI model."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['SKILL.md','v4/EXPERIMENT-ENGINE.md','v4/REVIEW-BOARD.md','v4/DEEP-SYSTEMS.md','v4/LEARNING-ENGINE.md','v4/RESEARCH-INTEGRITY.md','v4/SECURITY-LABS.md','v4/PROJECT-GATES.md','v4/BENCHMARK.md']
def audit():
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    text=(ROOT/'SKILL.md').read_text(encoding='utf8')
    failures=missing+[f'missing term: {x}' for x in ['authorization','hypotheses','Evidence','Egyptian Arabic'] if x.casefold() not in text.casefold()]
    return failures
if __name__=='__main__':
    faults=audit()
    if faults:
        print('FAILED:',*faults,sep='\n - ');sys.exit(1)
    print(f'PASS: {len(REQUIRED)} required files, 4 contract clauses checked (structural only)')
