# Browser listening — reading live social with Claude in Chrome

A method, not a connector. It costs nothing, needs no API key, no app review and no
stored credential, and it reaches things no analytics product exposes: engagement
counts, reply threads, and the argument happening around a topic right now.

**It only works in an interactive session.** See the hard limit at the bottom before
building anything on it.

---

## Why this beats web search for listening

Web search tells you what was **published**. It cannot tell you what is being
**argued about**, by whom, or how loudly. For an operator whose goal is authority
measured by who replies, the second is worth more.

On its first run this method found a viral post (110K views) citing figures that
contradicted the research report the week's content was built on — and caught a
scheduled post ninety minutes before it would have walked into that argument. Web
search had returned neither the post nor the contradiction.

## The method

**1. Load the tools in one call.** They are usually deferred:

```
ToolSearch: select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__tabs_close_mcp
```

If they do not load, stop — see **The hard limit**.

**2. Navigate straight to a search URL.** `navigate` called standalone creates the
tab group for you. Single-page apps need a beat to render: if the first read comes
back empty or with only chrome, wait ~4 seconds and read again.

**3. Use `read_page`, not `get_page_text`.** This matters more than it sounds.
`get_page_text` returns only the first `<article>` — one post. `read_page` with
`depth: 30` returns the whole timeline **including engagement counts**, which are
the entire point. `get_page_text` is for reading a single opened post.

**4. Open anything above ~10K views and read its replies.** The argument in the
replies is usually more useful than the post. It is where you find what the crowd
disputes, what it concedes, and what nobody is saying.

**5. Capture, for each signal:** the claim · the numbers cited · who is making it ·
the engagement · **and what nobody in the thread is saying that the operator has the
standing to say.** That last field is the one that becomes content.

**6. Cross-check against the operator's own sourcing.** If a viral post cites numbers
that contradict a report the team has already built content on, that is the most
important finding of the run. Flag it first, and check whether any scheduled piece is
now exposed.

**7. Close every tab.** Leave the browser as you found it.

## Read-only, always

Never post, like, reply, repost, follow, bookmark or DM from the operator's account.
Reading public search results in a browser is what a person does. Acting from their
account without them asking is not, and a personal account under an authority-building
programme is not one to risk. If a thread deserves a reply, write the reply as a draft
for the operator and let them send it.

## Query patterns

Rotate three to five per run rather than running all of them — freshness beats
coverage, and a scan nobody reads is wasted.

```
https://x.com/search?q=<topic>&f=live     Latest — what is happening now
https://x.com/search?q=<topic>            Top — what actually travelled
```

Build the set from the operator's pillars in `brand/brand-config.md`: their city,
their sector, their named category terms, the regulator or body that governs them,
and one deliberately adversarial query (`<sector> crash`, `<sector> scam`,
`<category> overrated`) — the criticism of a space is where the strongest contrarian
material lives.

## Mining the operator's own Instagram comments

The replies under his own posts are the highest-signal idea source in this system and
the cheapest to reach. They are his actual audience, asking him specifically, in their
own words. Web search cannot see them and no analytics product returns them.

Run this **before** the public scan — it is his audience, not the crowd's.

**1. Read the cursor first.** `state/comments-cursor.json` records, per post, the id of
the newest comment already mined and when. **Read forward only**, exactly like the
analytics cursor: open posts newest-first, stop at the first post where the newest
comment is one already recorded. On a normal day that is two or three posts.

**2. Open the profile**, `https://www.instagram.com/<handle>/`, and confirm the
signed-in account is his before reading anything. Same trap as analytics — an
assistant's browser returns an assistant's audience.

**3. Open each post since the cursor** and `read_page` it. Comments load lazily:
click "View all N comments", then keep expanding "Load more comments" until the count
stops rising or you reach roughly 200 on that post. Past that the tail is bots and
emoji and buys nothing.

**4. Capture only what could become a post.** Most comments are praise and cannot.
Four things can:

| what to look for | why it is an idea |
|---|---|
| **A question asked more than once**, across posts or accounts | Repetition is demand. Two people is a signal, four is a brief. |
| **An objection or a disagreement** | The counter-case, written by the person who holds it. Strongest contrarian material there is. |
| **A correction** — someone saying he got a detail wrong | Check it. If they are right, that is a correction post, which is his most persuasive shape. |
| **A request** — "do one on X", "how do you handle Y" | Demand stated outright. |

Record the comment verbatim, the handle, the post it sat under, and the date. **Their
phrasing matters more than your summary of it** — audience language is what the hook
should be written in.

**5. Never act from his account.** No replying, liking, hearting, pinning, deleting or
DMing, and no answering a question in-thread. If a comment deserves a reply, draft it
for him. Reading his own comment section is what he does; acting in it without asking
is not.

**6. Write the findings and then the cursor.** Append idea rows to
`library/idea-bank.md` at status `new`, sourced `ig-comments`. Then update
`state/comments-cursor.json` — **after** the rows land, never before, for the same
reason the analytics cursor is written last.

**A note on what this is not.** A comment is a lead, not a fact. Somebody asserting a
number in his comments is one person on the internet; it goes through the same
verification as any other claim before it becomes a row.

## Reading analytics this way

The same technique reads the operator's own analytics pages, which is a free
alternative to any analytics connector:

- LinkedIn creator analytics: `linkedin.com/analytics/creator/content/`
- LinkedIn per-post: the post's own "View analytics"
- Instagram: Meta Business Suite Insights, on web
- X: `analytics.x.com`, or the post's own view count

⚠ **Identity is the catch, and it is easy to miss.** This reads whatever account the
browser is *logged into*. For public search that does not matter — search results are
the same for everyone. For analytics it is the whole thing: an assistant's browser
returns the assistant's numbers, not the operator's. **Check who is logged in before
trusting a single analytics figure**, and if it is the wrong account, either the
operator runs the scan from their own browser or the numbers come through an API the
operator has granted once.

## The hard limit — read this before designing around the method

**Scheduled runs cannot do any of this.** A scheduled task starts a fresh session in
an isolated cloud container with no bridge to the operator's computer. The Chrome
tools are not merely disconnected there — they are **absent from the tool list
entirely**. This was probed directly at midday with the desktop app open, so it is not
a "Chrome was closed overnight" problem and leaving Chrome open changes nothing.

**Design consequence.** Split the pipeline:

| runs where | what it can do |
|---|---|
| **Interactive** — the operator invokes the team | Browser listening, comment mining, analytics reads, everything below |
| **Scheduled** — a cron fires it | Web search, project docs, drafting. **No browser.** |

A scheduled run that needs listening should say so plainly in its report — *"the live
scan needs an interactive run; type the command while Chrome is open"* — rather than
silently producing a thinner result and letting the operator assume it looked.

Do not retry the tool load, wait, or reschedule. It is structural.
