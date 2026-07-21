# Contributing

Thanks for helping improve 月薪喵.

## Before opening a pull request

1. Keep changes focused on this repository.
2. Do not add scraped artwork, sticker packs, brand assets, or material without a documented compatible license.
3. Run the asset build and validation commands from the README.
4. Confirm every used sprite cell contains artwork and every unused cell is fully transparent.
5. Keep the pet ID stable as `yuexin-miao`.

## Contributor attribution

GitHub contributor data must reflect people who actually authored commits in this repository.

- Use your own verified Git name and email.
- Add `Co-authored-by` only when that person materially contributed and agreed to be credited.
- Do not add AI tools, generators, or copied upstream identities as commit co-authors.
- Preserve an external work's license and attribution when it is included; do not fabricate contributor entries.

Before publishing a release, maintainers should inspect:

```bash
git shortlog -sne --all
git log --format="%an <%ae>" | sort -u
```
