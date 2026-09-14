# Posting automation — what exists, what was chosen

Researched September 2026. API terms on these platforms move fast; re-verify
anything here before building against it.

**Current decision: Route D — console pick, Claude posts through the browser.** No API
integration, no credentials, no scheduler. The Publisher publishes a console (see
`console.md`) carrying every variant. The operator clicks POST on the one he wants,
which records the pick; he then says "post" in chat and `post-runner` drives Claude in
Chrome to open the composer, fill his chosen copy and submit.

**The operator asked for this explicitly.** It is his browser, his accounts, his copy,
and his pick. The gates are what make it safe: nothing is posted that he did not choose,
the copy is never edited on the way to the composer, the signed-in account is verified
before anything is typed, Post is clicked once, and nothing is recorded as published
without a live URL read from the page.

Two things it is not, and must not drift into: it does not post anything he did not
pick, and it does not schedule. Both would turn a tool that acts on his decision into
one that makes decisions for him.

Do not build past this without him asking.

## What each platform actually permits

| Platform | Access | Friction |
|---|---|---|
| **LinkedIn feed** | `w_member_social` scope is **self-serve — no partner approval**. Posts on behalf of an authenticated member. | One OAuth grant by the account holder. No native scheduling, so the calendar holds timing. 24-hour rolling rate window, resets midnight UTC. |
| **Instagram** | Graph API content publishing. Business or Creator account only, linked to a Facebook Page. | **Meta app review required** to reach accounts beyond test users. Two-step publish: create media container, then publish. Volume caps per rolling window. |
| **X** | No free posting tier for new developers. Pay-per-use. | ~$0.015 per post without a link, ~$0.20 with a URL. Legacy Basic tier is $200/mo. Cheap at low volume unless posts carry links. |
| **LinkedIn articles / newsletters** | Not confirmed as exposed by the posting API. | Treat as manual until verified. |

## The three routes

**A — Packaged, human posts.** Zero setup, zero credentials, full control over what
goes live under the operator's name. One scheduled task per slot delivers the
finished caption, hashtags, alt text and asset list. **This is the active route.**

**B — LinkedIn direct.** Roughly a day of work. Self-serve LinkedIn app, one OAuth
grant, a script that posts from `content/calendar.md` and advances the idea-bank row
to `published`. Highest value per unit of effort when LinkedIn is the primary
platform. No app review, no vendor fee.

**C — Unified provider.** One integration covering every platform; the provider
absorbs Meta's app review. Options and list prices as of Sept 2026: Buffer API (free
for one key), Post for Me ($10/mo, 1,000 posts), Zernio ($19/mo), Postiz (free
self-hosted, $29/mo cloud), Ayrshare ($149+/mo), Outstand (~$0.01/post).

⚠ **Verify before committing to C:** several providers document LinkedIn *company
page* posting clearly but are vague about **personal profiles**, which is what this
operator posts from. Confirm personal-profile support in writing first.

## The blocker that decides the architecture

Not the API — the credential store. **API tokens must never go into project docs;**
the whole team can read those. A cloud session has no secret store of its own, so
tokens have to live either on a machine the team controls, or in a small always-on
service the scheduled run calls.

That decision is **open**. Design any future integration so the credential source is
swappable, and raise the question before writing the first line of a poster script.

## The cost of Route D, stated plainly

**Driving a real browser to click Post** breaks on any UI change, needs the machine
awake and signed in, and automating a personal account through a browser is not what
these platforms designed for. Those costs are real and the operator accepted them; they
are why `post-runner` reads the page at every step instead of trusting a selector, and
why a run that cannot confirm a URL reports a failure rather than a success.

**A published page still cannot drive the extension.** The extension is driven by Claude
inside a session, not by a web page — so the console's POST button records the pick and
the posting happens in the next chat turn, when the operator says "post". A button that
claimed to post directly from the page would be a button that does nothing.

## Ruled out

**Scheduling.** No cron, no scheduled task, no slot reminder — not for the engine and
not for a post. This system runs when he runs it. A scheduled run also has no browser
at all (see `browser-listening.md`), so a scheduled engine would be a thinner engine
that could neither listen nor post.

## Sources

- LinkedIn API reality check — https://www.socialcrawl.dev/blog/linkedin-data-api-2026
- Instagram Graph API guide — https://www.netrows.com/blog/instagram-graph-api-guide-2026
- X API pricing 2026 — https://www.socialcrawl.dev/blog/x-twitter-api-2026
- Multi-platform posting APIs — https://buffer.com/resources/social-media-api-multi-platform-posting/
