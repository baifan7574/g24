
import os
import requests
import json
import time
import re

# 搜索建议接口封装
def fetch_suggestions_google(query):
    try:
        url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)
        suggestions = json.loads(res.text)[1]
        return suggestions
    except:
        return []

def fetch_suggestions_bing(query):
    try:
        url = f"https://api.bing.com/osjson.aspx?query={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)
        suggestions = json.loads(res.text)[1]
        return suggestions
    except:
        return []

# 黑名单词
blacklist = ['wallpaper', 'hd', '4k', 'download', 'clipart', 'cartoon', 'anime', '中文', '英文', '发音', '图片', '高清', 'free', 'set', 'jj', 'emoji']

# 是否是合法英文关键词
def is_valid_keyword(kw):
    if any(bad in kw.lower() for bad in blacklist):
        return False
    if re.search('[一-鿿]', kw):  # 含中文字符
        return False
    if len(kw.strip()) < 8:
        return False
    if len(kw.split()) < 2:
        return False
    return True

# 搜索后合并建议
def get_suggestions(seed):
    combinations = [
        f"{seed} photo",
        f"{seed} aesthetic",
        f"{seed} photography",
        f"{seed} woman",
        f"{seed} female portrait"
    ]
    results = set()
    for combo in combinations:
        for fetcher in [fetch_suggestions_google, fetch_suggestions_bing]:
            suggestions = fetcher(combo)
            for s in suggestions:
                if is_valid_keyword(s):
                    results.add(s.strip())
        time.sleep(1)
    return list(results)

# 主流程
def main():
    input_dir = "./keywords"
    output_dir = "./output_keywords"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            seed = filename.replace(".txt", "")
            print(f"正在处理分类：{seed}")
            suggestions = get_suggestions(seed)
            cleaned = suggestions[:100]
            output_path = os.path.join(output_dir, filename)
            with open(output_path, "w", encoding="utf-8") as f:
                for kw in cleaned:
                    f.write(kw + "\n")
            print(f"生成关键词数：{len(cleaned)}，已保存：{output_path}")

if __name__ == "__main__":
    main()
