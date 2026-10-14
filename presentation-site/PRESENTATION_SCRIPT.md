

## 01 · Business context

Good afternoon and thank you for the opportunity to share how Codex can postively impact your business by reducing the risk in your growing Ad Delivery segment and improving the effeciency of your evolving engineering team.

Netflix expects about $3 billion in advertising revenue in 2026, roughly twice 2025. To meet this target, Netflix will need a highly productive engineering effort.

At the same time, technology and development expense rose 22% year over year in Q2, with personnel costs up $142 million. To me, this tells me that you are investing heavily in your people though it seems like the talent mix is also changing. In a recent interview, your CTO, Elizabeth Stone has described a strategy of continuing to invest in the senior engineers that you already have while also hiring earlier-career engineers with AI familiarity.

The opportunity is to help this evolving team move quickly while protecting the quality of a growing ad business.

## 02 · Protect monetization

I am sure you know this: Ad delivery connects an eligible request to a monetized impression.

What may not be so obvious is that a defect that suppresses fill can put that opportunity at risk, so resolving issues quickly matters.

We have helped countless companies improve their defect-resolution throughput - like Cisco, who reported 10–15 times higher defect-resolution throughput with Codex CLI in large repositories. This is illustrative of the outcome that we can provide for your busines as well.

## 03 · Introduce the Codex demonstration

Now I’ll show Codex working with an engineer on an ad-delivery defect. The Cisco case study demonstrated a huge increase in throughput and there are, of course, many factors that go into making that happen.

So let's start with a more simple outcome target: a goal to start with for this pilot will be to decrease the active engineering time per defect—from five hours to four, an effeciency gain of 20%.

After the demonstration, I’ll return to what that could mean for your engineering capacity and ad delivery.

**Run the Codex demo, then return to section 4.**

DEMO SCRIPT:

This demo will show one way Codex might help engineers diagnose and validate a fix while reducing release risk.

Issue: “The scenario is a fictional ad campaign that should remain eligible through its configured end time. The synthetic incident log shows no_fill at exactly that boundary. The ticket says the eligibility window should include both endpoints.”

Trace: “I’m asking Codex to follow the decision from the issue into the implementation and explain the suspected cause before changing anything.”

Regression: “Now I’m asking for a test of the exact boundary. It should fail against the current implementation, making the reported behavior reproducible.”

Fix: “With that failure established, Codex makes the smallest change and reruns the focused test file.”

Review: “The test passes, and the diff is limited to the end-time comparison and its regression test. An engineer reviews any proposed change before release."

## 04 · Business impact

During our last discovery call, you shared with me some metrics about what your team is dealing with today: 30 ad-delivery defects a month, five active engineering hours per defect, and eight issue-linked no-fill hours each month.

Based on other data that you have shared, running a scenario of: one million eligible requests per minute, a 5% defect-linked no-fill rate, a 70% monetizable share, and $30 net eCPM, each affected hour represents about $63,000 in revenue exposure. Across eight hours a month, that is $504,000 monthly, or about $6.05 million annualized. I understand that this scenario makes some assumptions and doesn't take every variable into account, but this gives you an idea of the kind of impact that using Codex to improve your defect-resolution process can have.

The productivity goal makes 30 engineer-hours a month available at this defect volume. The pilot measures active time per defect alongside issue-linked no-fill duration, escaped defects, reopened fixes, review effort, cost, and latency. That connects engineering efficiency to the value of ad delivery.

As a next step, I suggest that we run an engaged pilot with a subset of your engineering team. In this pilot, we will further refine the business case baseline, establish the testing and success criteria, set up Codex within your tool-set and train your teams on best-practices, and support your team throughout the pilot duration with Q&A sessions and additional resources.

After you watch this recording, please reach out to me for feedback and to set up next steps. I will follow up next week, if I don't hear from you before then.

Thank you.
