"""Transparent structural preflight, NOT an AI response quality assessment."""
import argparse
from pathlib import Path
REQUIRED=['SKILL.md','kernel/OPERATING-CONTRACT.md','kernel/VERIFICATION-LADDER.md',
'research/RESEARCH-ENGINE.md','investigation/CAUSAL-EXPERIMENTS.md','security/AUTHORIZED-LAB.md',
'reversing/BINARY-LAB.md','engineering/RELIABILITY-GATES.md','learning/MASTERY-LOOP.md',
'evals/SCORING.md','scripts/research_lab.py']
def inspect(root):
    errors=[]
    for name in REQUIRED:
        p=root/name
        if not p.is_file(): errors.append('missing '+name)
        elif p.stat().st_size<50: errors.append('too short '+name)
    skill=(root/'SKILL.md').read_text(encoding='utf-8') if (root/'SKILL.md').is_file() else ''
    if not skill.startswith('---\nname:'): errors.append('SKILL.md lacks YAML frontmatter')
    return errors
if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--selfcheck',action='store_true');a=parser.parse_args()
    errors=inspect(Path(__file__).resolve().parents[1]);print('PASS: structural preflight' if not errors else '\n'.join(errors));raise SystemExit(bool(errors))
