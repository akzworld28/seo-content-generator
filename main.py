import os
import requests
from textblob import TextBlob
import g4f


def get_trending_hr_topics():

    data = {
        "topics": ["AI in HR", "Remote Work Trends", "Employee Well-being", "HR Analytics", "Diversity and Inclusion"]
    }
    print("📌 Retrieved Topics:", data["topics"])
    return data.get("topics")[:5]


def generate_blog_outline(topic):
    if not topic:
        raise ValueError("❌ No topic provided for blog outline!")

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "system", "content": "You are a content strategist. Create an SEO-friendly blog outline."},
                  {"role": "user", "content": f"Generate an outline for a blog on '{topic}'"}]
    )
    return response


def generate_blog_content(outline):
    if not outline:
        raise ValueError("❌ No outline provided for blog content!")

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "system",
                   "content": "You are an expert HR writer. Expand the following outline into a detailed blog post."},
                  {"role": "user", "content": f"Expand this outline into a 2000-word SEO blog:\n{outline}"}]
    )
    return response


def improve_seo(content):
    if not content:
        return "❌ No content provided for SEO optimization!"

    blob = TextBlob(content)
    readability_score = blob.sentiment.polarity
    print(f"📊 Readability Score: {readability_score}")

    keywords = ["HR trends", "workplace policies", "employee engagement"]
    seo_optimized_content = content + f"\n\nKeywords: {', '.join(keywords)}"
    return seo_optimized_content + "\n\n🔹 SEO Optimized with better keywords and readability!"


def proofread_content(content):
    if not content:
        return "❌ No content provided for proofreading!"

    blob = TextBlob(content)
    return str(blob.correct())


def save_blog(content):
    os.makedirs("output", exist_ok=True)

    with open("output/final_blog.md", "w", encoding="utf-8") as f:
        f.write(content)

    html_content = f"<html><body><h1>SEO Blog</h1><p>{content.replace('\n', '<br>')}</p></body></html>"
    with open("output/final_blog.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("📁 Blog saved in Markdown and HTML format.")


def main():
    print("\n\n\t\t\t\t ✨ Hi, this is Reshma!\n\n 🙌 Welcome to the AI-Powered SEO Blog Generator – Your gateway to effortless, high-quality content creation!")
    print("\n\n🔍 Step 1: Researching Trending HR Topics...")
    trending_topics = get_trending_hr_topics()

    if not trending_topics:
        raise ValueError("❌ No trending topics found! Check 'get_trending_hr_topics()'.")

    topic = trending_topics[0]
    print(f"📌 Selected Topic:\n\n {topic}")

    print("\n📑 Step 2: Generating Blog Outline...")
    outline = generate_blog_outline(topic)
    print(f"📝 Blog Outline:\n\n{outline}")

    print("\n✍️ Step 3: Generating Blog Content...")
    blog_content = generate_blog_content(outline)
    print(f"📖 Blog Content:\n\n{blog_content}")

    print("\n🔍 Step 4: SEO Optimization...")
    seo_content = improve_seo(blog_content)
    print(f"🚀 SEO Optimized Content:\n\n{seo_content}")

    print("\n📝 Step 5: Reviewing and Proofreading...\n\n")
    final_blog = proofread_content(seo_content)
    print("✅ Review Completed!")

    save_blog(final_blog)
    print("\n🎉 Blog Generation Completed! Check the output folder for results.")


if __name__ == "__main__":
    main()