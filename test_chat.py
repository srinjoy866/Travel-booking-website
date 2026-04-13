#!/usr/bin/env python3
"""
Local KB tester for the project's `kb.json`.

Features added:
- Accepts `--message` as before.
- If `--message` is omitted, reads piped stdin (so you can do: `echo "text" | python test_chat.py`).
- If no stdin is piped and `--message` is omitted, prompts interactively.

Usage examples (PowerShell):
  & ".\.venv\Scripts\python.exe" ".\test_chat.py" --message "Paris museums"
  echo "Paris museums" | & ".\.venv\Scripts\python.exe" ".\test_chat.py"
  & ".\.venv\Scripts\python.exe" ".\test_chat.py"    # will prompt

No external network or API keys required.
"""
import argparse
import json
import os
import sys
from difflib import SequenceMatcher


def load_kb(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"KB file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def score_query(query, doc_text):
    # Simple normalized similarity between query and document text
    return SequenceMatcher(None, query.lower(), doc_text.lower()).ratio()


def get_query_from_args_or_stdin_or_prompt(parsed_args):
    # Priority: CLI arg > piped stdin > interactive prompt
    if parsed_args.message:
        return parsed_args.message.strip()

    # Check piped stdin
    try:
        if not sys.stdin.isatty():
            piped = sys.stdin.read().strip()
            if piped:
                return piped
    except Exception:
        pass

    # Interactive prompt as fallback
    try:
        return input('Enter message: ').strip()
    except EOFError:
        return ''


def main():
    parser = argparse.ArgumentParser(description='Local KB similarity tester')
    parser.add_argument('--message', '-m', required=False, help='Query to search in kb.json')
    parser.add_argument('--top', '-k', type=int, default=3, help='Number of top results to show')
    parser.add_argument('--kb', default='kb.json', help='Path to kb.json')
    args = parser.parse_args()

    query = get_query_from_args_or_stdin_or_prompt(args)
    if not query:
        print('No query provided. Use --message, pipe stdin, or type interactively.')
        sys.exit(1)

    try:
        kb = load_kb(args.kb)
    except Exception as e:
        print(f"Error loading KB: {e}")
        sys.exit(2)

    results = []
    for doc in kb:
        text = ' '.join(filter(None, [doc.get('title', ''), doc.get('text', '')]))
        s = score_query(query, text)
        results.append({'id': doc.get('id'), 'title': doc.get('title'), 'score': s, 'text': doc.get('text')})

    results.sort(key=lambda r: r['score'], reverse=True)
    top = results[: args.top]

    out = {
        'query': query,
        'top_matches': [
            {
                'id': r['id'],
                'title': r['title'],
                'score': round(r['score'], 4),
                'snippet': (r['text'][:300] + '...') if r['text'] and len(r['text']) > 300 else r['text']
            }
            for r in top
        ]
    }

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
