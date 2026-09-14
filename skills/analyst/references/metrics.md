# Metrics — what to ask for and what it means

## What to request per platform

Ask for exactly these fields. More is noise; fewer cannot be compared.

**Instagram** (Insights → per post)
`reach` · `impressions` · `saves` · `shares` · `comments` · `likes` ·
`follows from this post` · `profile visits`
Reels also: `plays` · `average watch time` · `retention %` if shown.

**LinkedIn feed** (post analytics)
`impressions` · `members reached` · `reactions` · `comments` · `reposts` ·
`follows` · `clicks` (if there is a link)

**X** (post analytics)
`impressions` · `engagements` · `bookmarks` · `reposts` · `replies` ·
`profile visits` · `follows`

**Threads** (insights)
`views` · `likes` · `replies` · `reposts` · `quotes` · `follows`

**Pulse** (article/newsletter analytics)
`views` · `reads` if shown · `reactions` · `comments` · `new subscribers`

## Which number to rank on

**The default is follows per 1,000 reached**, because `brand/brand-config.md` →
`## Targets` sets follower goals on every tracked platform. Use another row only when
the brand config's `goal` explicitly says something else.

| the operator's goal | rank on | why |
|---|---|---|
| **audience growth (default here)** | **follows per 1,000 reached** | the only number that compounds, and the only one the targets are written in |
| reach / distribution | saves + shares per 1,000 reached | what the platforms actually amplify |
| credibility / positioning | comments and their quality | who is replying matters more than how many |
| leads | profile visits and clicks per 1,000 reached | intent, not attention |

Likes are the weakest signal on every platform and should never decide anything.
Impressions measure distribution the platform gave you, not work you did.

## Normalise before comparing

Raw counts track follower count, not post quality. Always divide by reach:

```
save rate    = saves / reach * 1000
share rate   = shares / reach * 1000
follow rate  = follows / reach * 1000
engage rate  = (likes + comments + saves + shares) / reach * 100
```

Then express each post as a multiple of **this operator's own median for that
format**. "1.8× median save rate for carousels" is a usable sentence. "412 saves"
is not.

## Follower counts and pace

Log the **platform follower count once per readout**, per platform, with the date. It
is the only way to compute pace against the targets, and it is the one running total
worth keeping (see *What not to log* — per-post follower deltas still lag and confound;
this is a separate, coarser number used for one purpose).

```
followers = the raw count, read from the profile or supplied by the operator
added     = this reading minus the last one
pace      = added / days since the last reading
```

Report pace as arithmetic against the target and its horizon. If the pace does not
reach the number, say the pace does not reach the number — do not soften it, and do not
extrapolate a good week across a year.

**Targets are never published.** A goal reported as a result is the failure this
system guards hardest against; the same rule covers `brand/proof.md` → Targets.

## Sample-size discipline

| posts in a format | what you may say |
|---|---|
| 1–2 | nothing — record it, do not interpret it |
| 3–9 | "early signal", never "works" |
| 10–24 | "emerging pattern", with the counter-test named |
| 25+ | "established for this account" |

Never extrapolate from a single viral post. One outlier moves a median and tells
you almost nothing about what to do next; it usually reflects a distribution
accident rather than a repeatable move.

## Reading a spike honestly

When one post massively outperforms, check in this order before crediting the
content: was it shared by a large account; did it land in a search or hashtag surge;
was it a reply to something already spreading; did the operator post it at an
unusual time. If any of these hold, the lesson is about distribution, not craft —
label it that way in `patterns.md`.

## The retention question (Reels)

Average watch time matters more than plays. If retention drops before 3 seconds,
the hook failed — that is a `hook-writer` problem. If it drops between 3 and 8
seconds, the context beat is too long — a `script-writer` problem. Attribute the
drop to the beat where it happened so the right employee fixes it.

## What not to log

Follower count over time (it lags and confounds everything), vanity totals across
all posts, and any figure the platform labels "estimated". Log per-post numbers the
platform reports directly, and nothing derived that you cannot recompute.
