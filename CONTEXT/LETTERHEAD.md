# Waha Letterhead Specification

> Reference for generating cover letters on Waha's official letterhead. All cover letters (not email letters) MUST be produced as `.docx` files following this spec.

---

## Template-Based Approach

The letterhead uses floating positioned elements (logo, address text box) that are difficult to generate from scratch. Instead, **use the KIF template as a base**:

1. **Template file:** `alycias-edits-temp/Cover Letter - KIF.docx` (the canonical letterhead source)
2. **Method:** Copy the template, unpack as ZIP, replace body content in `word/document.xml` via text substitution, strip comments, repack
3. The template includes: positioned logo, address text box, footer with HR + contact line, embedded Lora and Outfit fonts

The build script at `/tmp/build-amos-letter.py` demonstrates the full approach (copy to CONTEXT if you want to persist it).

## Page Setup

| Property | Value |
|----------|-------|
| Paper size | US Letter (8.5" x 11") |
| Top margin | 1.0" (1440 DXA) |
| Bottom margin | 1.0" (1440 DXA) |
| Left margin | 0.9" (1296 DXA) |
| Right margin | 0.9" (1296 DXA) |
| Header distance | 0.5" (720 DXA) |
| Footer distance | 0.5" (720 DXA) |

## Fonts (Embedded in Template)

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Body text | Lora | 11pt (22 half-pt) | Regular | Black (#000000) |
| Header address block | Outfit | 9pt (18 half-pt) | Regular | Dark gray (#666666) |
| Footer contact line | Outfit Light | 10pt (20 half-pt) | Light (300) | Dark gray (#434343) |
| Sign-off name | Lora | 11pt | Regular | Black |
| Sign-off title & contact | Lora | 11pt | Regular | Black |

The template embeds these font files in `word/fonts/`:
- Lora (regular, italic, bold, boldItalic)
- Outfit (regular, bold)
- Outfit Light (regular, bold)

## Logo

- **File:** `CONTEXT/waha-logo.png` (1142 x 321px, RGBA PNG with transparent background)
- **Display size:** ~2.68" wide x ~0.79" tall (cx=2447925, cy=719978 EMU)
- **Position:** Floating anchor, page-relative: x=0.80" (731520 EMU), y=0.84" (766763 EMU)
- **Wrap:** Top and bottom (`wrapTopAndBottom`) -- body text flows below, not beside

## Header Address Block

- **Type:** Floating text box (WordprocessingShape), `wrapNone`
- **Position:** Page-relative: x=5.02" (4592955 EMU), y=0.91" (828675 EMU)
- **Size:** 2.68" x 1.15" (cx=2447925, cy=1047750 EMU)
- **Content (exact lines, right-aligned):**

```
522 W Riverside Ave #8369
Spokane, WA, 99201
United States
waha.app
```

- **Formatting:** Outfit 9pt, right-aligned, color #666666, single line spacing (240)

**Note:** The address block does NOT include the EIN. That goes in proposal documents, not the letterhead.

## Body Layout

### Document Structure (paragraph map from template)

| Paragraph | Content | Spacing |
|-----------|---------|---------|
| P0 | Letterhead (floating logo + address text box) | Document default |
| P1 | Date (`[Date]` placeholder) | after=80-200, line=276 |
| P2-P4 | Recipient address lines | after=0, line=276 |
| P5 | Last address line | after=200-360 (gap before salutation) |
| P6 | Salutation | after=200, justified |
| P7-Pn | Body paragraphs | after=160, line=264, justified |
| Pn+1 | Closing phrase | after=200 (signature gap) |
| Pn+2 | Signer name | after=0, before=0 |
| Pn+3 | Title | after=0, before=0 |
| Pn+4 | Email | after=0, before=0 |
| Pn+5 | Phone | after=0, before=0 |

### Salutation
- "Dear [Title] [Last Name]," or "Dear [Name] and the [Foundation] Team,"
- See `CONTEXT/STYLE_GUIDE.md` for salutation rules
- Not bold (template KIF version is bold, but that's optional)

### Body Paragraphs
- Font: Lora 11pt
- Alignment: Justified (`w:jc val="both"`)
- Line spacing: 1.1x (`w:line="264"`) -- tighter than the 1.15x default to help one-page fit
- Paragraph spacing: 8pt after (`w:after="160"`)

### Sign-Off Block
- Closing phrase (e.g., "Respectfully," / "With gratitude," / "In Christ,")
  - Use "In Christ," for explicitly Christian foundations
  - Use "With gratitude," or "Respectfully," for secular or mixed foundations
  - Match the foundation's culture from `03-VOCABULARY-AND-FRAMING`
- Spacing: 10pt after closing phrase (`w:after="200"`)
- Each subsequent line on its own paragraph (after=0, before=0):
  - Signer name (e.g., "Vince Kanagaraj")
  - Title (e.g., "Partnerships Director, Waha")
  - Email (e.g., "vince@waha.app")
  - Phone (e.g., "+1 (586) 306-4273")

## Footer

Located in `word/footer1.xml` (a Word footer section, appears on all pages):

1. Empty centered spacer paragraph
2. Horizontal rule: VML rect, fillcolor #A0A0A0, height 1.5pt, `o:hr="t"`
3. Contact line: `contact@waha.app   *   +1 (425) 243-8884`
   - Font: Outfit Light 10pt, color #434343, centered

## Cover Letter vs. Email Letter

| Feature | Cover Letter | Email Letter |
|---------|-------------|--------------|
| Letterhead | Full (logo, address, footer) | None |
| Body font | Lora (serif) | Arial (sans-serif) |
| Output format | `.docx` on letterhead | `.md` only (pasted into email) |
| Date line | Yes | No |
| Recipient address block | Yes (formal) | No |
| Signature gap | Yes (10pt after closing) | No |
| Title/heading | None (starts with date) | Include "Email Letter - [Foundation]" heading |

**How to decide:** Check `04-APPLICATION-REQUIREMENTS`. If the submission method is email, use the email letter format. If it's mail, online portal with attachment, or unspecified, use the cover letter format on letterhead.

## PDF Export Note

Do NOT export directly from Google Docs to PDF -- it makes the letterhead blurry. The correct workflow:

1. Generate the `.docx` file with letterhead
2. Open in Microsoft Word or Apple Pages
3. Export to PDF from there

## One-Page Target

Cover letters should fit on one page whenever possible. If the letter runs to a second page:
- The letterhead header appears only on page 1 (floating elements are page-1-anchored)
- The footer appears on all pages
- Tighten the prose before expanding to a second page
- If still overflows, reduce body `w:line` from 264 to 240 (single spacing) and `w:after` from 160 to 120

**Note:** LibreOffice renders slightly differently from Word/Google Docs. A letter that barely overflows in LibreOffice may fit on one page in the target applications. Always verify the final layout in Word or Google Docs.

---

*Source of truth: Alycia's formatted cover letters in `alycias-edits-temp/` (Johnson Foundation, KIF). Logo extracted from those documents.*
