# SEO and GEO standard for band9ai.org

**Status:** the only SEO and GEO file for this site. Read this before publishing any new page that should rank or support a sale.

**Applies to:** every public page on `band9ai.org`. Product, pricing, and checkout stay on `band9ai.com`.

**What this file is:** the working rules for Search and for Google’s generative AI features (AI Overviews and AI Mode). “GEO” (generative engine optimization) and “AEO” (answer engine optimization) are names other people use. Google treats both as ordinary SEO. There is no second playbook.

**What this file is not:** a ranking file. Google Search does not read a special Markdown, `llms.txt`, or other “AI text” file to decide who appears. Keeping this document in the repo neither helps nor hurts rankings. Do not add it to the sitemap, and do not link it from public guides.

Last compiled: 2026-10-04.

This file restates official Google Search Central guidance so the team can apply it. The Google pages remain the authority. They are licensed CC BY 4.0. If a Google page and this file ever disagree, follow the Google page and update this file.

## Sources

| Topic | Official page | Google’s last update |
| --- | --- | --- |
| Generative AI features on Google Search | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 2026-07-10 |
| Using generative AI content on your site | https://developers.google.com/search/docs/fundamentals/using-gen-ai-content | 2026-10-01 |
| Spam policies | https://developers.google.com/search/docs/essentials/spam-policies | 2026-08-28 |
| Search Essentials | https://developers.google.com/search/docs/essentials | 2025-12-10 |
| How AI Overviews and AI Mode treat sites | https://developers.google.com/search/docs/appearance/ai-features | — |
| Helpful, people-first content | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | — |
| Google’s view of AI-generated content | https://developers.google.com/search/blog/2023/02/google-search-and-ai-content | — |

Related pages named in that guidance: Search technical requirements, crawling best practices, crawl budget, JavaScript SEO, image SEO, video SEO, technical SEO guide, maintaining SEO, evaluating third-party SEO advice, Merchant Center, Google Business Profile, Business Agent, agent-friendly website practices, Universal Commerce Protocol, Search Quality Rater Guidelines sections 4.6.5 and 4.6.6, and the Generative AI performance report in Search Console.

## How Google’s generative features actually work

People use generative AI to find information. Google’s AI Overviews and AI Mode are built on the same ranking and quality systems as Google Search. They highlight pages already in the Search index. Two mechanisms matter:

**Retrieval-augmented generation (grounding).** The system retrieves relevant, current pages from the Search index, reads the specific information on those pages, and writes a response from that material. The response shows prominent, clickable links to the pages that support it. A page that is not indexed, or that is not eligible to show a snippet, cannot be a supporting link.

**Query fan-out.** The model issues several related queries at once so it can fetch more results. A question such as “how to fix a lawn that’s full of weeds” might also pull “best herbicides for lawns”, “remove weeds without chemicals”, and “how to prevent weeds in lawn”. Fan-out is Google’s behavior. It is not a brief to publish a separate page for every related phrasing.

Eligibility for a supporting link in AI Overviews or AI Mode: the page is indexed and eligible to appear in Google Search with a snippet. There are no extra technical requirements beyond Search. Meeting every requirement still does not guarantee crawling, indexing, or serving. Appearing in Search is free.

A site must also be included in Search generative AI features in Search Console to be eligible for display in those features.

## The one test before a sales page

Google’s systems are built to connect people with pages they find satisfying. Before publishing, answer this: **would a visitor who came here directly feel the page was worth the visit?**

A page can sell. The sale has to come after a real answer. On this site that means:

1. The page explains one IELTS question a candidate actually has, with a worked example and the limits of the claim.
2. The explanation is specific to this publisher: how the band average works, how a Writing criterion caps a task, or how a Band9AI practice estimate differs from an official score.
3. The commercial step is a clear next action on `band9ai.com` (free Reading + Writing Task 2 estimate, Reality Check, Skill Fix, or Complete), matched to the question the page just answered.
4. The page says, where the claim depends on it, that Band9AI is not the British Council, IDP, or Cambridge, and that a practice estimate is not an official IELTS score.

A page whose main job is to sit on a keyword and push a click does not pass the test. Volume of pages does not raise quality.

## band9ai.org and band9ai.com

A clean folder structure tracks the quality of the foundation. It is early as a prediction about traffic. Meeting the rules in this file means the site is ready to be crawled. It does not mean the site is already taking queries away from anyone, including `band9ai.com`.

`band9ai.org` explains how a score is built. `band9ai.com` is the mock, the price, and the checkout. That split helps the company when a guide answers a question the product site does not already answer, then sends the reader to the matching IELTS offer. The two sites compete on the day both of them publish the same explanation for the same query. Google then has two of this company’s pages to choose from, and the one that ranks may be the one that does not sell.

Before a new `.org` URL:

1. Confirm `band9ai.com` does not already answer that question. If it does, do not publish a second version here.
2. Point the offer at the matching IELTS product: free Reading + Writing Task 2 estimate, Reality Check, Skill Fix, or Complete. A TOEFL guide may link there only when the page says the offer is an IELTS estimate, not a TOEFL score.
3. After launch, watch Search Console for which URLs actually get impressions. That report, not the folder structure, shows whether this site is taking queries or only ready to.

## Search Essentials

Three parts decide whether web content (pages, images, video, or other public material) can appear and do well:

1. **Technical requirements.** The minimum Google needs in order to show a page. Most sites already meet them. This site must keep pages crawlable, indexable, and eligible for a snippet.
2. **Spam policies.** Behaviors that can lower a page or an entire site, or remove it. They apply to ordinary results and to generative AI responses. They apply to every site Google finds, including Google’s own properties. The full list is below. Google may also act on spam that is not named in the list.
3. **Key best practices.** The few actions that most affect how a page looks and ranks:
   - Create helpful, reliable, people-first content.
   - Use the words people would type, in the title, the main heading, alt text, and link text.
   - Make links crawlable so Google can discover the rest of the site.
   - Tell the right people the site exists, in communities where that is welcome.
   - Follow the specific best practices for images, video, structured data, and JavaScript.
   - Turn on Search features that fit the page.
   - If something must stay out of Search, use the proper control (`noindex`, `nosnippet`, `data-nosnippet`, `max-snippet`, or a robots rule). Robots.txt for Googlebot is how crawling for Search is controlled, including for AI features.

Violations are detected by automated systems and, when needed, by human review that can become a manual action. Report other sites through a search quality user report. Those reports train detection. They are not a ranking lever for this site.

## Content rules for pages that should rank

Creating unique, compelling, useful content matters more for long-term visibility in generative AI search than any other item in Google’s guide.

### Unique point of view

Google’s systems read many sources. A page that only restates what is already everywhere is easy to skip. A first-hand review, a worked scoring example, or an explanation from operating the product is a point of view. Write from what this publisher actually knows. Do not recycle another site’s article, and do not publish text a model could emit with no added experience.

For Band9AI, the point of view is the scoring mechanic and the product’s limits: overall band as the average of four skills rounded to the nearest half band; Writing criteria averaged inside a task, with Task 2 weighted more than Task 1; published calibration figures with their definitions. Official band descriptors and test rules stay attributed to IELTS. Do not copy them in bulk.

### Non-commodity, helpful, reliable, people-first

Commodity content is common knowledge anyone could write, such as a generic “7 tips” list. It adds little. Non-commodity content is a specific expert or experienced take, such as a real decision and what it changed.

On this site, a non-commodity page shows the arithmetic, the criterion, or the measurement, then says what the reader should do next. A generic IELTS tips page does not.

People-first means the page is useful if the reader never came from Google. Experience, expertise, authoritativeness, and trustworthiness (E-E-A-T) are the qualities Google’s systems are designed to reward. The “why” of a page is help for the visitor. Publishing mainly to collect search visits is misaligned with those systems. Publishing with automation mainly to manipulate rankings violates the spam policies.

### Structure for readers

Write for people. Use paragraphs, sections, and headings that make the page easy to follow. Put the direct answer where a reader (and a snippet) can find it, then the worked detail, then the next step. There is no ideal length. Shorter and longer pages both work when they match the subject and the reader.

### Images and video

Generative AI features can surface relevant images and video, so a page can appear as more than a blue link. Add high-quality, relevant images or video when they genuinely explain the point (a score table, a worked average, a short walkthrough). Follow Google’s image SEO and video SEO documentation. Decorative filler does not count.

Alt text describes the image for people. It is also reviewed when content is generated with AI. Do not stuff keywords into alt text.

### Do not manufacture query variants

It is tempting to publish a page for every way someone might ask, including fan-out queries. Doing that mainly to manipulate rankings or generative AI responses violates the scaled content abuse policy. It also fails as a strategy: a large number of pages does not make a site more relevant. Google can judge relevance when the query and the page’s main wording do not match exactly. Synonyms and general meaning are understood. Chasing every long-tail phrasing is unnecessary.

One strong page per real question. Link related guides to each other. Let Google fan out.

### Structured data

Structured data is not required for generative AI search, and there is no special schema.org type to add for AI Overviews. Keep using structured data that matches the visible text, because it supports rich results. Validate it. Follow the general structured-data guidelines and the rules for the specific feature. On this site that currently means Organization, WebSite, Article, BreadcrumbList, FAQPage, and Speakable only when the page actually contains that content.

FAQ markup repeats questions the page answers in public view. Do not invent FAQ entries for queries the page does not answer.


### Accuracy

Models predict a likely word sequence from training data. They do not look up facts. Outputs can be wrong (hallucinations). A person must fact-check every AI-assisted page before it is published, including:

- `<title>`
- meta description
- structured data
- image alt text

Anything that can appear in a Search result gets the same review as the body. Numbers on this site (band averages, rounding, prices, calibration claims, dates) are checked against the publisher’s own sources and, where the claim is about the official test, against IELTS. Invented statistics, fake testimonials, and fake official scores are prohibited.

### Tell readers how it was made, when that helps

If automation substantially created the content, consider saying so in a way that fits the audience: what was automated, and why. Useful questions from Google’s helpful-content guidance:

- Is the automation obvious from a disclosure or from the page itself?
- Is there background on how automation was used?
- Is there a reason automation was useful here?

Add that context when a reader would reasonably ask how the page was made. Do not give a model an author byline. The publisher is BAND9AI HUMAN SYSTEMS INC.

### Merchant and product assets

Google Merchant Center has its own rules for AI-generated content. AI-generated images must carry IPTC `DigitalSourceType` metadata of `TrainedAlgorithmicMedia`. AI-generated product title and description attributes must be specified separately and labeled as AI-generated. Guides on this domain are not Merchant Center feeds. Product feeds, if any, live with the product on `band9ai.com` and follow those policies.

## Technical structure

Google’s AI systems can only use what Search can find and process. Existing technical SEO still matters.

- **Indexed and snippet-eligible.** Required for generative AI features.
- **Included in Search Console’s generative AI features setting.** Required for display there.
- **Crawlable.** Generative models use publicly accessible, crawlable content. `robots.txt` on this site allows `/`. Keep important text in the HTML, not only inside blocked scripts or images.
- **Internal links.** Other guides must be reachable by crawlable links. IELTS guides live in `/ielts/`. TOEFL iBT guides live in `/toefl/`. The home page links both. Old root URLs for the first IELTS guides redirect to `/ielts/`. List every indexable URL in `sitemap.xml`.
- **TOEFL pages do not invent a TOEFL product.** Band9AI’s paid practice on band9ai.com is IELTS. A TOEFL guide may link there only when it says the offer is an IELTS estimate, not a TOEFL score.
- **Crawl budget.** This site is small. The large-site crawl-budget guide matters only if the site later becomes very large or updates constantly. Until then, a current sitemap and the Page indexing report are enough.
- **Semantic HTML.** Perfect markup is not required. Google understands imperfect HTML. Use semantic elements when they help people, including screen-reader users.
- **JavaScript.** Google can process JavaScript that is not blocked. Framework sites are harder to get right. These guides are static HTML, which is the simpler path. If a page becomes client-rendered, follow JavaScript SEO and keep the main text available without a workaround that looks like cloaking.
- **Page experience.** Readable on phones and desktops, reasonably fast, with the main answer easy to separate from navigation and offers.
- **Duplicates.** Duplicate URLs waste crawling and annoy readers. One canonical URL per guide. Do not publish the same explanation under several slugs, cities, or keyword spellings.
- **Search Console.** Verify the property and use it to find technical problems. The technical SEO guide and the “maintaining your site’s SEO” guide are the references.

Controls, when a page must not appear or must not contribute a snippet: `noindex`, `nosnippet`, `data-nosnippet`, `max-snippet`. Use them deliberately. A sales guide that should rank stays indexable and snippet-eligible.

## Local business and product details

Generative AI responses can include product listings and local-business information when that fits the query. Merchant Center feeds and a Google Business Profile can surface products and services in AI responses and in other Search results. Business Agent is a conversational experience on Google Search for brands that want customers to chat with them. Universal Commerce Protocol is an emerging way for Search agents to do more.

Use those only where the business actually has the asset. Do not invent a store listing, a fake local page, or a city landing page to chase “IELTS tutor in {city}” queries. That pattern is doorway abuse.

This domain publishes guides. The commercial destination is `https://band9ai.com`.

## Practices Google says to ignore

These circulate under AEO and GEO labels. They are not how Google Search works. Third-party SEO or GEO advice has to be checked against Google’s page on evaluating third-party SEO advice. No outside tool has access to Google’s internal ranking or AI systems.

**`llms.txt` and special AI markup.** Google Search does not use `llms.txt`, other machine-readable AI files, special markup, or Markdown to decide visibility. Google may crawl many file types besides HTML. Crawling a file does not mean the file is treated as a ranking signal. This repo has an `llms.txt` for other systems. Leave it if those systems use it. Do not expect it to change Google rankings, and do not create more “AI files” for that purpose.

**Chunking.** There is no requirement to break pages into tiny pieces for AI. Google can take the relevant part of a page that covers more than one topic. Make the length fit the reader.

**Rewriting for the model.** There is no special style, keyword density, or long-tail list required for generative AI search.

**Inauthentic mentions.** AI features can reflect what the web says in blogs, videos, and forums. Buying or manufacturing mentions is not a quality strategy. Ranking systems prefer high-quality content, and other systems block spam. Generative features depend on both.

**Over-focusing on structured data.** Covered above. Keep valid markup that matches the page. Do not add markup solely in the hope of an AI citation.

## Measuring results

Use the Generative AI performance report in Search Console for visibility in generative AI features on Google Search and Discover. Ignore tools that promise rankings from “internal” Google metrics. A tool is fine as a workflow aid. Its advice still has to survive this file and the official pages.

Judge a page by whether the right readers arrive, stay long enough to understand the answer, and continue to `band9ai.com` when they want the estimate or the paid check. A citation that never earns a satisfied visit is not the goal.

## Agentic experiences

AI agents can act for a person, such as booking or comparing specifications. Browser agents may open the site, read a visual rendering, inspect the DOM, and use the accessibility tree. If this becomes relevant and there is time, follow Google’s agent-friendly website practices. Protocols such as Universal Commerce Protocol are emerging for Search agents.

Preparation that already matches this standard: real text in the page, semantic structure, working links, an accessibility tree that matches what people see, and no content that exists only for a bot.

## Spam policies (all of them)

Spam here means techniques meant to deceive users or to manipulate Search into featuring content, including manipulation of generative AI responses. A site that violates these policies can rank lower or disappear. The policies below are the ones Google lists. Each subsection ends with the rule for this website.

### Cloaking

Cloaking is showing users and search engines different content in order to manipulate rankings and mislead people. Examples: a travel page for the crawler and a different offer for the visitor; keywords inserted only when the user agent is a search engine.

If JavaScript or images are hard for a crawler, make that content available to users and to Google through the recommended methods. Do not serve a special version to Googlebot.

A hacked site often cloaks so the owner does not notice. Fix the hack.

A paywall is not cloaking when Google can see the full gated content the same way a subscriber can, and Flexible Sampling guidance is followed. These guides are public. Do not gate the article and show Google a different full text.

**This site:** the HTML the reader sees is the HTML Google sees.

### Doorway abuse

Doorways are sites or pages built to rank for specific, similar queries. They send people to intermediate pages that are less useful than the real destination. Examples:

- Many sites with slight URL and homepage differences, to cover more queries.
- Many domains or pages aimed at regions or cities that all funnel to one page.
- Pages generated only to funnel visitors into the useful part of a site.
- Nearly identical pages that resemble search results more than a browseable site.

**This site:** do not create city pages, band-score variant pages, or “IELTS {keyword}” pages that repeat the same pitch. Each URL earns its place with different substance. Internal links may lead to `band9ai.com` after the answer. The guide itself is the destination for the question it answers.

### Expired domain abuse

Buying an expired domain and repurposing it mainly to manipulate rankings, with content of little or no value to users. Examples Google gives: affiliate content on a former government domain, commercial medical products on a former charity medical domain, casino content on a former school domain.

**This site:** `band9ai.org` is used for these guides because they belong to this publisher. Do not park unrelated content here to borrow the domain’s history.

### Hacked content

Content placed without permission through a security hole. It produces poor results and can infect visitors.

- **Code injection.** Malicious JavaScript in pages or iframes.
- **Page injection.** New spam or phishing URLs added to the site. Existing pages can look normal.
- **Content injection.** Hidden links or hidden text, via CSS or HTML, or cloaking, so crawlers see what the owner misses.
- **Redirects.** Some visitors are sent to a bad page depending on referrer, user agent, or device. A click from Google redirects, a direct visit does not.

**This site:** keep the host locked down. Review unexpected files, scripts, and redirects. Google’s hacked-site documentation is the repair guide.

### Hidden text and link abuse

Placing content only so search engines see it and people do not. Examples: white text on white, text behind an image, CSS positioning off-screen, font size or opacity set to 0, a link on a single tiny character such as a hyphen.

These patterns are allowed, because they help people:

- Accordions and tabs that show and hide extra content.
- Slideshows that cycle images or paragraphs.
- Tooltips that appear on interaction.
- Text for screen readers that improves that experience.

**This site:** offers, disclaimers, and links are visible. No hidden keyword blocks.

### Keyword stuffing

Filling a page with keywords or numbers to manipulate rankings. They often appear as an unnatural list or out of context. Examples: phone-number lists with no real value, blocks of city and region names, repeating a phrase until the sentence sounds unnatural.

**This site:** the title, H1, and opening answer use the real query language once, clearly. The body then teaches. Do not paste band numbers, city names, or “IELTS” in a list to rank.

### Link spam

Links created mainly to manipulate rankings. Google’s examples:

- Buying or selling links for ranking, including money for links or for posts that contain links, goods or services for links, and free products in exchange for a write-up with a link.
- Excessive “link to me and I’ll link to you” exchanges, or partner pages that exist only to cross-link.
- Automated programs or services that create links.
- A contract or terms of service that forces a link and does not let the other site mark it as a non-ranking link.
- Text ads or text links that pass ranking credit.
- Advertorials and native advertising where payment buys a link that passes ranking credit, or optimized anchor text in articles, guest posts, or press releases.
- Low-quality directory or bookmark links.
- Keyword-rich, hidden, or low-quality links inside widgets spread across sites.
- Footer or template links widely distributed on other sites.
- Forum comments with optimized links in the post or signature.
- Low-value content created mainly to manipulate linking and ranking signals.

Buying and selling links for advertising and sponsorship is normal. Those links are allowed when the `<a>` tag uses `rel="nofollow"` or `rel="sponsored"`.

**This site:** do not buy ranking links. A paid mention, sponsorship, or affiliate link uses `rel="sponsored"` or `rel="nofollow"`. Guest posts, if any, exist for readers and do not carry optimized commercial anchors as the point of the post. Outbound links to IELTS, methodology, and `band9ai.com` are real citations and product paths, not a link scheme.

### Machine-generated traffic

Automated queries to Google, including scraping results to check ranks, or other automated access without express permission. It wastes resources and breaks the spam policies and the Google Terms of Service.

**This site:** do not scrape Google for rank tracking. Use Search Console.

### Malicious practices

A mismatch between what the user expects and what happens, including harm to security or privacy.

- **Malware.** Software or apps built to harm a device, its software, or its users, including installs without consent and viruses. A download can be malware even when the owner did not mean it.
- **Unwanted software.** Deceptive or unexpected behavior, such as changing the homepage or other browser settings, or leaking personal information without proper disclosure. Follow Google’s Unwanted Software Policy.
- **Back-button hijacking.** Manipulating history or the browser so Back does not return the person to the page they came from.

**This site:** no forced downloads, no browser hijacks, no deceptive installers.

### Misleading functionality

Sites that pretend a tool or service works and then do not provide it. Examples: a fake generator that claims to give app-store credit, or a page that claims to merge PDFs, count down, or define words, and instead dumps the visitor into deceptive ads.

**This site:** every claim about the free estimate and the paid checks must be true. Say what is scored, what is not, and that the result is a practice estimate. Do not imply an official IELTS result, a guaranteed band, or a feature the product does not have.

### Scaled content abuse

Many pages generated mainly to manipulate rankings, not to help users. The problem is unoriginal content with little or no value, whatever the production method. Examples:

- Generative AI or similar tools used to create many pages without added value.
- Scraping feeds, search results, or other content into many pages, including synonym substitution, translation, or other obfuscation that still adds little.
- Stitching pages together from other sites without added value.
- Multiple sites meant to hide that the content is scaled.
- Many pages that make little sense to a reader but contain search keywords.

If such content is on a property you control, exclude it from Search.

**This site:** new pages are commissioned one at a time, each with original explanation. A batch of AI pages aimed at keyword coverage is forbidden, even if each file looks “unique” at a glance.

### Scraping

Taking other sites’ content, often automatically, and republishing it to manipulate rankings. Examples:

- Republishing without original content or value, including without citing the source.
- Copying and changing it only slightly, including synonym swaps or automated rewrites.
- Reproducing someone else’s feed without a unique benefit.
- Sites that mainly embed or compile other people’s videos, images, or media without substantial added value.

**This site:** do not republish IELTS forums, other tutors’ articles, or official materials as our own. Short quotation with attribution is for evidence. The rest of the page is original.

### Site reputation policy

This policy applies when third-party content is published on a host site mainly to borrow ranking signals the host earned with its own content, so the third-party page ranks better than it would alone. Google has specific rules for the European Economic Area (EEA).

Third-party content is content from a separate entity: users, freelancers, white-label providers, or anyone not employed by the host. Third-party content by itself is fine. It conflicts with the policy only when the main reason it is on the host is the host’s existing ranking signals.

Inconsistent examples:

- An educational site hosting a sponsored payday-loan review written by a third party that distributes the same page to many sites.
- A medical site hosting a low-quality third-party “best casinos” advert that is not part of the site, placed there to rank on the medical site’s signals.

Not inconsistent:

- Wire services and press-release services.
- News publications syndicating news from other news publications.
- Sites built for user content, such as forums and comment sections.
- Columns, opinion, and other editorial work.
- Advertorial or native advertising whose purpose is to share something with that publication’s readers, rather than to host it for ranking.
- Affiliate links used properly, or third-party ad units, across a page.

Google usually assumes a page, including a new page, matches the quality of the rest of the domain. If a portion looks out of line, the site can go to human review. Consequences depend on where the user is:

- **Outside the EEA:** the pages can receive a manual action in results shown outside the EEA.
- **Inside the EEA:** the pages can be categorized as separate from the main domain and ranked on their own merits, without that manual action. Similar content competes with similar content.

Affected sites are notified in the Manual actions report and the Search Console message center. They can appeal with a reconsideration request. Eligible sites can then take disputes to mediation.

Human review, when it happens, asks whether the host contributed enough input, editorial oversight, or control for the content to count as part of the main site, so the rank matches how users experience the page. The review is global. Factors, none of which is necessary or sufficient alone:

- Presentation: design, formatting, typography, and UX consistent with the host.
- Quality: problems on that page that the main site does not have.
- Authorship: a clear owner or responsible editor, and whether other signs contradict that claim.
- Whether the same or nearly the same content appears on other sites.

Other evidence can count, including pages that are third-party marketing material placed to manipulate ranking.

Google’s worked examples, in short:

- **Unlikely to act:** a coupons section run with a specialist, on a different CMS, filed under the publisher’s own categories, disclosed as commercial, editorially owned by the publisher with the partner, cross-linked from the publisher’s own articles, curated, reachable from the main navigation, and supported by the publisher’s normal contact path.
- **Likely to act (outside the EEA):** an unaffiliated affiliate article, no author, no responsible editor, no commercial disclosure, not in any section, not linked from the home page or section menus, and duplicated from a third-party marketplace.
- **Unlikely to act:** a new cooking section by a named freelancer under the newsroom’s editorial control, branded like the rest of the site, with a selection of interviews or recipes made for that site even if the freelancer writes elsewhere and the affiliate links resemble other publications.

**EEA questions Google answers:**

- A manual action under this policy outside the EEA does not affect ranking inside the EEA, and that outside action is not a ranking signal inside the EEA.
- There is no duty to `noindex` content that has a manual action outside the EEA. Leaving it indexable is not a ranking factor inside the EEA, and it is not treated as evasion or a repeat violation.
- Previous manual actions under this policy for EEA results are lifted. Those pages are no longer demoted in EEA results. They may later be categorized as separate and ranked on their own merits. That is not automatic. A past action is not a ranking signal.
- “Separate from the main domain” means Google drops the assumption that those pages share the domain’s quality. They do not instantly lose the main site’s signals. Over time, systems can learn to rank the parts independently, which can change how each part ranks, including when one part’s site-wide signals improve. The categorization itself is not a ranking signal.
- In the EEA, reconsideration requests are answered on a short timeline with more detail, and alternative dispute resolution is available.

**This site:** guides are first-party. A freelancer piece, if used, is commissioned for this site, edited here, branded here, and bylined. Do not host third-party affiliate or advertorial pages to borrow this domain’s signals. Do not syndicate the same article onto a network of other domains.

### Sneaky redirects

A redirect sends the visitor to a different URL than the one requested. A sneaky redirect does that to show users and search engines different content, or to show users something that does not meet the need they arrived with. Examples: one document for crawlers and a different destination for people, or a normal desktop page and a mobile redirect to a spam domain.

Legitimate redirects: moving the site, merging several pages into one, sending a logged-in user to an internal page. The test is whether the redirect is meant to deceive users or search engines.

**This site:** `band9ai.org` guides stay on their canonical URLs. Links to `band9ai.com` are ordinary links, visible as the next step, not a surprise redirect of the guide itself. Use redirects only for real URL changes, and point them at the equivalent page.

### Thin affiliation

Product pages whose descriptions and reviews are copied from the merchant, with no original content or added value. Also, affiliate programs that distribute the same material across many sites, so the pages look like one template repeated across URLs, domains, or languages. A results page full of those copies is a poor experience.

Affiliate sites that add value are fine: extra price context, original reviews, real testing and ratings, useful navigation, comparisons.

**This site:** do not build thin “best IELTS course” pages that copy other sellers. If a guide mentions the paid product, the value is the explanation on the page. The product link is the continuation, and any paid external endorsement is marked `sponsored` or `nofollow`.

### User-generated spam

Spam that users add through a channel meant for them, often without the owner noticing: open hosting accounts, forum posts, blog comments, uploads on file hosts. If comments or accounts are added later, moderate them. Google’s public-area abuse guidance and hacked-site guidance apply.

**This site:** these guides do not currently take public posts. If that changes, new accounts and comments are moderated, and obvious spam is removed.

### Other practices that can demote or remove pages

**Legal removals.** A large volume of valid copyright removals against a site can demote other content from that site, so people are more likely to reach the original. Similar signals apply to defamation, counterfeit goods, and court-ordered removals. Child sexual abuse material is removed when identified, and sites with a significant proportion of it are demoted as a whole.

**Personal information removals.** A large volume of personal-information removals tied to exploitative removal practices can demote other content from the site. The same pattern on other sites can be demoted too. Similar treatment can apply to a large volume of removals involving doxxing, explicit personal imagery shared without consent, or explicit non-consensual fake content.

**Policy circumvention.** Continuing to evade spam or content policies can restrict or remove eligibility for features such as Top Stories and Discover, and can remove more of the site from Search. Examples: new or existing subdomains, subdirectories, or sites used to keep violating, and other methods meant to continue the same behavior.

**Scam and fraud.** Imposter sites, false business information, or other false pretenses. Automated systems try to keep scam pages out of Search. Examples: impersonating a known business to take payment, or fake “official support” pages with fake contact details.

**This site:** publish only what this company can stand behind. Do not impersonate IELTS, the British Council, IDP, or Cambridge. Do not republish their materials. The company identification already used on the site is BAND9AI HUMAN SYSTEMS INC., Toronto.

## Page checklist

Use this for every new URL.

**Reader**

- [ ] One real question, answered in the first screen.
- [ ] Original explanation, with a worked example where the topic is a score or a rule.
- [ ] Limits stated: practice estimate versus official IELTS score, and no false affiliation.
- [ ] A visitor who never sees the offer still got the answer.
- [ ] Headings match the sections. Paragraphs are readable on a phone.

**Search and generative AI**

- [ ] Unique `<title>` and H1 in the words a candidate would use.
- [ ] Meta description describes this page, and was fact-checked.
- [ ] Canonical URL on `https://band9ai.org/...`.
- [ ] Indexable, snippet allowed, main text in HTML.
- [ ] Crawlable links to related guides and, where it helps, to the matching `band9ai.com` page.
- [ ] In `sitemap.xml` with an accurate `lastmod`.
- [ ] Structured data matches visible content and validates.
- [ ] Images, if any, are relevant, compressed, and honestly described in alt text.
- [ ] No second URL for a spelling variant, a city, or a fan-out query.

**Commercial**

- [ ] `band9ai.com` does not already answer this question.
- [ ] The offer matches the page (free estimate, Reality Check, Skill Fix, or Complete).
- [ ] Price and what is included are accurate on the day of publishing.
- [ ] Paid or affiliate links use `rel="sponsored"` or `rel="nofollow"`.
- [ ] The guide does not redirect away as soon as it loads.

**Production**

- [ ] If a model drafted any of it, a person checked facts, titles, descriptions, schema, and alt text.
- [ ] No scraped paragraphs, no stitched pages, no hidden text.
- [ ] The page looks and reads like the rest of band9ai.org.
- [ ] After launch, watch Search Console impressions for this URL, including the Generative AI performance report. Impressions, not the folder it sits in, show whether the page is taking queries.

## What to do next, in order

1. Keep foundational SEO: clear technical structure, snippet-eligible indexed pages, and unique useful content.
2. Prefer non-commodity pages that a candidate can use the same day.
3. Ignore AEO/GEO tactics: chunking, extra AI text files for Google, manufactured mentions, and query-variant farms.
4. Measure with Search Console impressions and the Generative AI performance report. The report shows whether a URL is taking queries. The folder structure does not.
5. Revisit agent-friendly practices only when agents are actually part of how customers buy.

## Staying current

Google asks site owners to follow:

- Google Search Central blog
- Google Search Central on LinkedIn and on X
- Google Search Central Help Forum
- Google Search Central on YouTube

When one of the source pages in the table at the top changes, update this file in the same change as any new guide that depends on it. Do not keep a second SEO or GEO document.
