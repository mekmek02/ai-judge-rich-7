"""ai-judge-rich-7 entry writer.

Writes the fixed PLAN text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) with no trailing newline added.

Edge note: one paid hour pays three times - claim, tool, care -
so finished code ships first and the same hour is counted once.
"""

import os

PLAN = """Judge: count only money I can already see. No code until escrow shows. Fiverr, Upwork, Stripe need a human ID; cold mail unread.
Live board: make.fun 7 open, ~$3,800 pots, 130 paid, 5 free; Bountycaster, Dework, Gitcoin, Algora, escrow first.
Days 1-2: TypeScript kit (auth, webhook, CSV, tests) + scanner. $10 credit, $10 gas, $80 reserve.
Claims: max 2, each a tested PR in 24h; 10 drafts, duel pairs twice, send the winner, revise on provisional grade.
Leg 2: each kit module $19-29 on Gumroad; every paid claim also sells $19/mo care; buyers bring 2 referrals.
Math: 22 claims, half paid, 11 x $140 = $1,540, less 30% ~$1,078; tools 18 x $19 = $342; care 6 x $19 = $114. Day 30: $100-$20+$1,534 ~$1,615. Floor: 4 paid ~$392 + tools $114: ~$590.
Kill: below its paid line after 2 tries, drop it; no accepted claim in 5 days, bounties only; under 2 care signups in 14 days, drop care.
Edge: one paid hour pays three times - claim, tool, care; rivals pitch promises, mine ships finished code first."""


def main():
    if not 1 <= len(PLAN) <= 1000:
        raise ValueError("PLAN must be 1-1000 characters, got %d" % len(PLAN))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
