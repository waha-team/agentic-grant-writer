#!/usr/bin/env python3
"""
Build the Amos Family Foundation cover letter using Alycia's KIF letterhead as template.
Replaces body content while preserving the letterhead, fonts, footer, and formatting.
"""

import shutil
import zipfile
import os
import re

SRC = "/home/yeshu/projects/grants/alycias-edits-temp/Cover Letter - KIF.docx"
WORK = "/tmp/amos-letterhead-build"
OUT = "/home/yeshu/projects/grants/06-to-be-submitted/japanese-dmc--amos-family-foundation/06-COVER-LETTER - Amos Family Foundation - japanese-dmc.docx"

# Clean workspace
if os.path.exists(WORK):
    shutil.rmtree(WORK)
os.makedirs(WORK)

# Unpack the KIF docx
with zipfile.ZipFile(SRC, 'r') as z:
    z.extractall(os.path.join(WORK, "unpacked"))

doc_path = os.path.join(WORK, "unpacked", "word", "document.xml")

with open(doc_path, 'r', encoding='utf-8') as f:
    xml = f.read()

# ── Step 1: Strip all comments ──
# Remove comment range markers and references from document.xml
xml = re.sub(r'<w:commentRangeStart[^/]*/>', '', xml)
xml = re.sub(r'<w:commentRangeEnd[^/]*/>', '', xml)
xml = re.sub(r'<w:r[^>]*><w:commentReference[^/]*/></w:r>', '', xml)
# Also remove runs that only contain a commentReference
xml = re.sub(r'<w:r\b[^>]*>\s*<w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>\s*<w:commentReference[^/]*/>\s*</w:r>', '', xml)

# ── Step 2: Replace date ──
xml = xml.replace(
    '<w:t xml:space="preserve">[Date]</w:t>',
    '<w:t xml:space="preserve">March 31, 2026</w:t>'
)

# ── Step 3: Replace recipient address lines ──
xml = xml.replace(
    '<w:t xml:space="preserve">Kristin Zelov and  Patty Erickson</w:t>',
    '<w:t xml:space="preserve">Daniel P. Amos Family Foundation</w:t>'
)
xml = xml.replace(
    '<w:t xml:space="preserve">Kingdom Investment Foundation</w:t>',
    '<w:t xml:space="preserve">PO Box 5346</w:t>'
)
# The Tucson line has trailing spaces
xml = re.sub(
    r'<w:t xml:space="preserve">Tucson, AZ 85739\s*</w:t>',
    '<w:t xml:space="preserve">Columbus, GA 31906</w:t>',
    xml
)
xml = xml.replace(
    '<w:t xml:space="preserve">USA</w:t>',
    '<w:t xml:space="preserve">United States</w:t>'
)

# ── Step 4: Replace salutation (remove bold, change text) ──
# The KIF salutation is bold. Remove bold from the paragraph and run properties.
# Find the salutation paragraph and replace it entirely

# Template for a normal (non-bold) body paragraph
def make_body_para(text, para_id, spacing_after="160"):
    """Create a body paragraph XML with Lora font, justified, proper spacing."""
    # Escape XML entities
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Convert smart quotes to XML entities
    text = text.replace('\u2019', '&#x2019;')  # right single quote / apostrophe
    text = text.replace('\u201C', '&#x201C;')  # left double quote
    text = text.replace('\u201D', '&#x201D;')  # right double quote
    text = text.replace('\u2018', '&#x2018;')  # left single quote

    return f'''<w:p w:rsidR="00000000" w:rsidDel="00000000" w:rsidP="00000000" w:rsidRDefault="00000000" w:rsidRPr="00000000" w14:paraId="{para_id}"><w:pPr><w:spacing w:after="{spacing_after}" w:before="0" w:line="264" w:lineRule="auto"/><w:jc w:val="both"/><w:rPr><w:rFonts w:ascii="Lora" w:cs="Lora" w:eastAsia="Lora" w:hAnsi="Lora"/></w:rPr></w:pPr><w:r w:rsidDel="00000000" w:rsidR="00000000" w:rsidRPr="00000000"><w:rPr><w:rFonts w:ascii="Lora" w:cs="Lora" w:eastAsia="Lora" w:hAnsi="Lora"/><w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'''

# ── Step 4b: Tighten spacing for one-page fit ──
# Reduce date line spacing (after 200 → 80)
xml = xml.replace('w:after="200" w:line="276" w:lineRule="auto"',
                   'w:after="80" w:line="276" w:lineRule="auto"', 1)
# Reduce last-address-line gap to salutation (360 → 200)
xml = xml.replace('w:after="360"', 'w:after="200"')

# ── Step 5: Replace the salutation + body + closing paragraphs ──
# Strategy: Find P6 (salutation) through P14 (closing) and replace them all at once.
#
# We'll use regex to find from the salutation through to the closing,
# matching by the unique text content.

# First, let's find the salutation paragraph (contains "Dear Ms. Zelov")
salutation_pattern = r'<w:p\b[^>]*>[^§]*?Dear Ms\. Zelov[^§]*?</w:p>'
# That won't work well with regex on XML. Let me use a different approach.

# Split on known anchors. The salutation starts after the "USA" address line.
# And the closing "With gratitude," is followed by "Vince Kanagaraj".

# Find the salutation paragraph - it contains "Dear Ms. Zelov"
sal_start = xml.find('Dear Ms. Zelov')
# Walk backward to find the <w:p that contains it
sal_p_start = xml.rfind('<w:p ', 0, sal_start)

# Find "With gratitude," paragraph end
closing_text_pos = xml.find('With gratitude,')
closing_p_end = xml.find('</w:p>', closing_text_pos) + len('</w:p>')

# Extract everything between sal_p_start and closing_p_end (salutation + body + closing)
old_section = xml[sal_p_start:closing_p_end]

# Build the new section
new_paragraphs = []

# Salutation (non-bold)
new_paragraphs.append(make_body_para(
    "Dear Mr. Amos, Mrs. Amos, and the Amos Family Foundation Board,",
    "10000007", spacing_after="160"
))

# Body paragraph 1
new_paragraphs.append(make_body_para(
    "My name is Vince Kanagaraj, and I serve with Waha, a Christian organization that strengthens the well-being of communities by equipping ordinary believers to share Scripture through simple, audio-guided Bible discovery groups. I am writing because we believe the Japanese people, whom your family has served through Aflac for more than fifty years, represent one of the world\u2019s most spiritually underserved populations. Japan is the fourth-largest economy on earth, yet fewer than 1% of its 125 million people are Christian. The church is aging, with the average pastor over sixty and the average congregation numbering just thirty. Most Japanese believers have simply never been equipped to share their faith with their neighbors.",
    "10000008"
))

# Body paragraph 2
new_paragraphs.append(make_body_para(
    "Waha\u2019s Disciple Making Course addresses that barrier directly. It is a nine-week training that gives believers the confidence and tools to gather a small group, listen to Scripture together, and discuss what God reveals. No seminary degree is needed. No special preparation. In London, an American church planter spent years trying to get new believers to share their faith in a culture where people assumed \u201Can expert should be the one to do ministry.\u201D Before a sabbatical, he introduced the Disciple Making Course to his team. When he returned three months later, multiple discovery groups had started without him, young leaders had developed confidence to lead on their own, and people were being discipled whom he had never met. Japan\u2019s church faces that same cultural barrier, and we believe this tool can help break it open.",
    "10000009"
))

# Body paragraph 3
new_paragraphs.append(make_body_para(
    "The Japanese translation is complete, with 99% approved in our localization platform. A grant of $7,500 would fund the remaining audio production by native Japanese speakers and cultural adaptation, creating a permanent discipleship resource for 125 million Japanese speakers. Waha is a 501(c)(3) nonprofit that collaborates with Biblica, Wycliffe, and YouVersion to deliver Scripture to communities worldwide, and our tools are now used by more than 82,000 people across 170 countries.",
    "1000000A"
))

# Body paragraph 4
new_paragraphs.append(make_body_para(
    "Your foundation\u2019s mission to glorify God and His Son by strengthening the well-being of individuals and communities resonates deeply with what we are working to accomplish in Japan. If this project aligns with your current funding priorities, I have enclosed a full proposal and budget for your review and would welcome the opportunity to share more about what God is doing through this work.",
    "1000000B"
))

# Closing (with larger spacing after for signature gap)
new_paragraphs.append(make_body_para(
    "Respectfully,",
    "1000000C", spacing_after="200"
))

new_section = '\n'.join(new_paragraphs)

# Replace the old section with the new one
xml = xml[:sal_p_start] + new_section + xml[closing_p_end:]

# ── Step 6: Fix sign-off format ──
# Change "Partnerships Director | Waha" to "Partnerships Director, Waha"
xml = xml.replace('Partnerships Director | Waha', 'Partnerships Director, Waha')

# ── Step 6b: Tighten top margin for one-page fit ──
# The floating letterhead is page-positioned, so reducing top margin
# gives more room for body text without affecting the header layout.
# Margins stay at original 1" - the letterhead is page-positioned so unaffected

# ── Step 7: Write the modified document.xml ──
with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(xml)

# ── Step 8: Clear comments.xml ──
comments_path = os.path.join(WORK, "unpacked", "word", "comments.xml")
if os.path.exists(comments_path):
    # Write a minimal empty comments file
    with open(comments_path, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        f.write('<w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
                'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml">'
                '</w:comments>')

# ── Step 9: Repack as docx ──
unpacked_dir = os.path.join(WORK, "unpacked")

with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as zout:
    for root_dir, dirs, files in os.walk(unpacked_dir):
        for filename in files:
            filepath = os.path.join(root_dir, filename)
            arcname = os.path.relpath(filepath, unpacked_dir)
            zout.write(filepath, arcname)

file_size = os.path.getsize(OUT)
print(f"Created: {OUT}")
print(f"Size: {file_size:,} bytes")
print("Done!")
