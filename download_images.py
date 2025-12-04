#!/usr/bin/env python3
"""
Download images from <img> tags in markdown files and convert to markdown image syntax.

Usage:
    python download_images.py [--dry-run]

Options:
    --dry-run   Show what would be done without actually downloading or modifying files
"""

import os
import re
import sys
import urllib.request
from pathlib import Path


def find_md_files(directory: Path) -> list[Path]:
    """Find all markdown files matching chapter*.md pattern."""
    return sorted(directory.glob("chapter*.md"))


def extract_img_tags(content: str) -> list[tuple[str, str, str]]:
    """
    Extract img tags from content.
    Returns list of (full_match, src_url, alt_text).
    """
    pattern = r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*/?>|<img[^>]*alt="([^"]*)"[^>]*src="([^"]+)"[^>]*/?>'
    results = []

    for match in re.finditer(pattern, content):
        full_match = match.group(0)
        if match.group(1):  # src comes before alt
            src_url = match.group(1)
            alt_text = match.group(2)
        else:  # alt comes before src
            alt_text = match.group(3)
            src_url = match.group(4)
        results.append((full_match, src_url, alt_text))

    return results


def get_chapter_number(filename: str) -> str:
    """Extract chapter number from filename."""
    match = re.search(r'chapter(\d+)', filename)
    if match:
        return match.group(1)
    # Handle prologue, epilogue etc.
    if 'prologue' in filename:
        return '0'
    if 'epilogue' in filename:
        return '8'
    return '0'


def download_image(url: str, save_path: Path) -> bool:
    """Download image from URL to save_path."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(save_path, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"  Error downloading {url}: {e}")
        return False


def process_markdown_files(base_dir: Path, dry_run: bool = False) -> None:
    """Process all markdown files in the directory."""
    figures_dir = base_dir / "figures"

    if not dry_run:
        figures_dir.mkdir(exist_ok=True)

    md_files = find_md_files(base_dir)

    if not md_files:
        print("No chapter*.md files found.")
        return

    print(f"Found {len(md_files)} markdown files")
    print(f"Figures directory: {figures_dir}")
    print("-" * 50)

    # Track image counter per chapter
    chapter_counters: dict[str, int] = {}

    for md_file in md_files:
        print(f"\nProcessing: {md_file.name}")

        content = md_file.read_text(encoding='utf-8')
        img_tags = extract_img_tags(content)

        if not img_tags:
            print("  No <img> tags found")
            continue

        print(f"  Found {len(img_tags)} <img> tags")

        chapter_num = get_chapter_number(md_file.name)
        if chapter_num not in chapter_counters:
            chapter_counters[chapter_num] = 0

        new_content = content

        for full_match, src_url, alt_text in img_tags:
            chapter_counters[chapter_num] += 1
            img_num = chapter_counters[chapter_num]

            # Generate new filename: pic{chapter}-{num}.png
            new_filename = f"pic{chapter_num}-{img_num}.png"
            new_path = figures_dir / new_filename
            relative_path = f"figures/{new_filename}"

            # Generate markdown image syntax
            # Use alt text if available, otherwise use filename
            display_alt = alt_text if alt_text and alt_text != "image" else f"図{chapter_num}-{img_num}"
            markdown_img = f"![{display_alt}]({relative_path})"

            print(f"  [{img_num}] {src_url[:60]}...")
            print(f"      -> {relative_path}")

            if not dry_run:
                # Download image
                if download_image(src_url, new_path):
                    print(f"      Downloaded successfully")
                else:
                    print(f"      Download failed, skipping replacement")
                    continue

            # Replace in content
            new_content = new_content.replace(full_match, markdown_img)

        if new_content != content:
            if dry_run:
                print(f"  Would update {md_file.name}")
            else:
                md_file.write_text(new_content, encoding='utf-8')
                print(f"  Updated {md_file.name}")

    print("\n" + "-" * 50)
    if dry_run:
        print("Dry run complete. No files were modified.")
    else:
        print("Processing complete.")


def main():
    dry_run = '--dry-run' in sys.argv

    # Get the directory where the script is located
    script_dir = Path(__file__).parent.resolve()

    print("Image Download and Conversion Script")
    print("=" * 50)
    print(f"Working directory: {script_dir}")
    if dry_run:
        print("MODE: Dry run (no changes will be made)")
    print()

    process_markdown_files(script_dir, dry_run)


if __name__ == "__main__":
    main()
