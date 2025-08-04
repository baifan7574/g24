
import os
import requests
import json
import time

# 设置关键词源（Google + Bing + YouTube）
def fetch_google_suggestions(query):
    try:
        url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)
        suggestions = json.loads(res.text)[1]
        return suggestions
    except:
        return []

def fetch_bing_suggestions(query):
    try:
        url = f"https://api.bing.com/osjson.aspx?query={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)
        suggestions = json.loads(res.text)[1]
        return suggestions
    except:
        return []

def fetch_youtube_suggestions(query):
    try:
        url = f"https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)
        suggestions = json.loads(res.text)[1]
        return suggestions
    except:
        return []

# 关键词过滤器
def clean_keyword(kw):
    banned_words = ['wallpaper', 'download', 'hd', '4k', 'free']
    return all(b not in kw.lower() for b in banned_words)

def get_all_suggestions(seed):
    results = set()
    for fetcher in [fetch_google_suggestions, fetch_bing_suggestions, fetch_youtube_suggestions]:
        suggestions = fetcher(seed)
        for s in suggestions:
            if clean_keyword(s):
                results.add(s.strip())
        time.sleep(1)  # 防止频繁请求被封
    return list(results)

# 主程序
def main():
    input_dir = "./keywords"
    output_dir = "./output_keywords"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            seed = filename.replace(".txt", "")
            print(f"正在处理分类：{seed}")
            suggestions = get_all_suggestions(seed)
            unique_keywords = suggestions[:100]
            output_path = os.path.join(output_dir, filename)
            with open(output_path, "w", encoding="utf-8") as f:
                for kw in unique_keywords:
                    f.write(kw + "\n")
            print(f"生成关键词数：{len(unique_keywords)}，已保存：{output_path}")

if __name__ == "__main__":
    main()
