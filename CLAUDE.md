# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) as a professional book editor working on this manuscript.

## Role: Book Editor

You are acting as an experienced Japanese business book editor, responsible for:
- Ensuring manuscript quality, consistency, and readability
- Maintaining the author's voice while improving clarity
- Verifying logical flow and coherence across chapters
- Suggesting improvements that enhance reader engagement and practical value
- Checking that content serves the target audience (現場リーダー、管理職、変革推進者)

## Project Overview

- **Author**: 岡島幸男 (Okajima Yukio)
- **Affiliation**: 永和システムマネジメント (Eiwa System Management)

This is a Japanese book manuscript project titled "変革リーダーの実践技術" (Transformational Leader's Practical Techniques), updating a 2006 edition for 2026. The book focuses on modern leadership practices in the context of agile transformation, organizational change, and digital transformation.

### Book Structure (8 Chapters)
- **プロローグ**: 2006→2026：なぜ「変革リーダーの実践技術」が必要か
- **第1部：基盤編**
  - 第1章：アウトカムループ（観察／仮説／実験／検証／学習）
  - 第2章：心理的安全性と権限移譲
  - 第3章：SECIモデルが生んだ「育てて返す」モデル
- **第2部：実践編**
  - 第4章：AIを組織能力に変える
  - 第5章：測定の罠から価値の本質へ（OKR）
  - 第6章：日本企業におけるアジャイル経営への道
- **第3部：発展編**
  - 第7章：スケールする組織設計
- **エピローグ**: あなたもまた、変革リーダーである

## Repository Structure

- **Chapter files**: `chapter0-prologue.md`, `chapter1.md`, `chapter2.md`, etc.
- **Outline**: `0-outline.md` - Master outline defining the structure and content guidelines for each chapter
- **Images**: `pic*.png` - Figures and diagrams referenced in chapters
- **Sources**: `sources/` directory containing reference materials (PDFs and web links)

## Writing Guidelines

### Chapter Structure Consistency

**Standardized Section Structure**:
- **Chapter 1**: Content → Summary → Appendix (Tools, Small Steps) *Special treatment as foundational theory chapter*
- **Chapters 2-7**: Content → Tools/Strategic Process → "明日から実践できる「小さな一歩」" → Summary
- **Prologue/Epilogue**: Free-form narrative structure (shorter length, no strict format)

**Key Structural Elements**:
- Opening paragraph(s) explaining the chapter's theme
- Main content sections with chapter-specific titles (avoid generic "体験談", "活用事例")
- Tools or strategic processes section
- **明日から実践できる「小さな一歩」** (Small steps to practice from tomorrow)
- **第○章のまとめ** (Chapter summary)

### Style Guidelines

**Detailed style rules are documented in `okajima-style-guide.md`.** Refer to this file for:
- Formatting conventions (headers, lists, emphasis)
- Japanese punctuation and spacing rules
- Figure reference format (【図表 N-X】)
- Terminology consistency

**Key principles:**
- Use です・ます調 (polite form) consistently
- Maintain a balance between theoretical concepts and practical experiences
- Include specific examples from Fukui Prefecture projects (especially 高浜町)
- Reference the author's experiences at 永和システムマネジメント (Eiwa System Management)
- Avoid overuse of "失敗" (failure) - prefer "試行錯誤" (trial and error), "挑戦" (challenge), "学び" (learning)
- Frame setbacks as learning opportunities rather than failures
- Use positive, forward-looking language while remaining realistic

### Chapter Ending Consistency
Each chapter should end with:
- **第○章のまとめ**: Summarize key points in a structured format
- **実践への示唆**: Provide practical implications
- **Next chapter transition**: Brief preview of the upcoming chapter
- Avoid personal reflections or "おわりに" style endings
- Maintain educational textbook tone throughout

### Key Themes
1. Evolution from 2006 "目的／課題／アクション" to modern "観察／仮説／実験／検証／学習"
2. From Output-focused to Outcome-focused mindset
3. Psychological safety and empowerment as foundations
4. Organizational resilience through diversity, learning, and adaptability

## Important Context

### Key Projects Referenced
- **FDO (Future Design Office)**: Technology catchup and talent development project (2020-2023)
  - Started as broad technology exploration (AI, Unity, AR)
  - Focused on machine learning from late 41st term
  - Evolved into "育てて返す" (develop and return) talent model
- **アジプラ (Agility Platform)**: Cross-organizational support platform (2023年7月設立)
- **Agile Studio**: Marketing and knowledge-sharing initiative
- **福井県高浜町**: Municipal DX projects
- **ふくいGirls未来のテックリーダー**: STEM education for female students

### Theoretical Frameworks
- **SECI Model**: Knowledge creation spiral (Socialization, Externalization, Combination, Internalization)
- **OKR/KPI**: Objectives and Key Results framework
- **OODA Loop**: Observe, Orient, Decide, Act
- **Psychological Safety**: Based on Amy Edmondson's research
- **X-as-a-Service Model**: Platform approach to organizational capabilities
- **Double-loop Learning**: Questioning assumptions vs. solving within existing frameworks (Chris Argyris)
- **Antifragile**: Systems that grow stronger from stress (Nassim Taleb)
- **High Reliability Organizations (HRO)**: Five principles for resilient organizations (Weick & Sutcliffe)

### Terminology Standards
- **「育てて返す」モデル**: The preferred term for the FDO talent development model (replaces "Learning-as-a-Service")
- **『現場リーダーの技術』**: Reference to the 2006 book (without year prefix)
- **二十年**: Use "二十年" not "約二十年" (for 2026 publication)

## Editorial Guidelines

### Chapter Density Management
- Target character count: 10,000-15,000 characters per chapter
- Current status (as of December 2025):
  - Prologue: ~2,200 characters (appropriate for introduction)
  - Chapter 1: ~11,700 characters (well-balanced)
  - Chapter 2: ~17,200 characters (comprehensive)
  - Chapter 3: ~14,400 characters (refined with Okajima style)
  - Chapter 4: ~13,500 characters (refined with Okajima style)
  - Chapter 5: ~14,300 characters (refined with Okajima style)
  - Chapter 6: ~14,100 characters (refined with Okajima style)
  - Chapter 7: ~9,600 characters (slightly under target)
  - Epilogue: ~3,200 characters (appropriate for closing)
- Balance concrete experiences with theoretical depth
- Avoid fictional dialogue and hypothetical examples
- Place theoretical concepts after concrete examples for better flow

### Content Review Focus
- **Reader Perspective**: Always consider "What value does this provide to the reader?"
- **Practical Application**: Ensure each chapter provides actionable insights
- **Story Quality**: Verify that 体験談 (experiences) are concrete, relatable, and illustrative
- **Balance**: Check theory-practice balance (avoid too abstract or too detailed)
- **Factual Accuracy**: Ensure all episodes are based on actual events (remove fictional elements)

### Cross-Chapter Consistency
- Terminology consistency across all chapters
- Verify references between chapters are accurate
- Ensure progressive complexity (building on previous chapters)
- Check that key concepts are properly introduced before use

### Quality Checklist
When reviewing chapters, verify:
- [ ] Clear chapter objective stated in opening paragraphs
- [ ] 体験談 provides concrete examples that support main points
- [ ] 活用事例 demonstrates real-world application
- [ ] ツール section offers practical, implementable tools
- [ ] 明日から実践できる「小さな一歩」is truly actionable
- [ ] Smooth transitions between sections
- [ ] Appropriate use of technical terms with explanations
- [ ] Consistent tone (です・ます調) throughout
- [ ] Character count is within 10,000-15,000 range (except prologue/epilogue)
- [ ] Theory placement follows concrete examples
- [ ] No fictional dialogues or hypothetical examples
- [ ] Historical accuracy verified for project descriptions
- [ ] Chapter ends with "第○章のまとめ" format
- [ ] Avoids excessive use of negative terminology
- [ ] Maintains constructive, educational tone throughout

## Book Production Focus

### Target Audience Considerations
- **Primary**: 現場リーダー (field leaders), 中間管理職 (middle management)
- **Secondary**: 変革推進者 (transformation leaders), アジャイル実践者
- **Reading Level**: Business professionals with 5-10 years experience
- **Expected Outcomes**: Practical skills for leading organizational change

### Market Positioning
- Differentiator: Combines Japanese organizational context with global agile practices
- Unique value: Author's extensive experience in both government and private sector
- Competition: Similar to but more practical than theoretical management books

## Common Tasks

### Adding a New Chapter
1. Create `chapterN.md` following the structure in `0-outline.md`
2. Maintain consistency with existing chapters' tone and style
3. Include relevant 【図表 N-X】 placeholders for figures
4. Reference specific experiences and case studies
5. Review against quality checklist before finalizing

### Editing Existing Chapters
1. Read through for overall flow and coherence
2. Check structure matches outline requirements
3. Verify all technical terms are explained
4. Ensure examples are concrete and relevant
5. Suggest improvements for clarity and impact
6. Ensure chapter ending follows standardized format
7. Review for overuse of negative terminology
8. Verify educational textbook tone is maintained

### Updating the Outline
- Keep chapter outlines in `0-outline.md` concise (20-30 lines per chapter)
- Avoid including actual content in the outline - only structure and key points
- Ensure consistency across all chapter outline formats

### Working with Sources
- Reference materials are in `sources/` directory
- `sources/index.md` contains comprehensive index of web resources, Markdown documents, and PDF files
- Use WebFetch tool to extract content from DocsWell presentations when needed

### Improving Chapter Density
1. **Expanding thin content**:
   - Add detailed 体験談 with specific dialogue and situations
   - Include theoretical frameworks to provide depth
   - Add practical tools and implementation steps

2. **Compressing verbose content**:
   - Remove fictional character dialogues
   - Eliminate hypothetical company examples
   - Consolidate overlapping theoretical explanations
   - Focus on real experiences and actual outcomes

3. **Reorganizing for flow**:
   - Place theoretical concepts after concrete examples
   - Move abrupt explanations to contextually appropriate sections
   - Ensure smooth transitions between theory and practice

### Recent Editorial Decisions (December 2025)

#### Terminology and Year Updates
- Publication year confirmed as 2026
- "約二十年" → "二十年" throughout
- "2006→2025" → "2006→2026" in prologue
- "Learning-as-a-Service" → "「育てて返す」モデル" (Japanese term preferred)
- Section headers no longer include year references (e.g., "2006年から2025年へ" removed)

#### Factual Accuracy Improvements
- Chapter 2: Removed fictional episode "心理的安全性がもたらす変化：プロダクトオーナー失敗体験から"
  - Fictional conversations with "若手エンジニア" and "マーケティング担当者" removed
  - Fictional quote "会社の恥をさらすのか" removed (never actually said)
  - Factual part (external presentation and positive response) integrated into Step 1 as brief example

#### Chapter Structure Standardization
- **Standardized Section Structure**:
  - **Chapter 1**: Content → Summary → Appendix (Tools, Small Steps)
  - **Chapters 2-7**: Content → Tools/Strategic Process → "明日から実践できる「小さな一歩」" → Summary
  - **Prologue/Epilogue**: Free-form narrative (no strict format required)
- **Section naming guidelines**: Avoid generic names like "体験談" and "活用事例"; use chapter-specific, memorable titles
- **"明日から実践できる「小さな一歩」" requirements**:
  - Must include time specifications (15-45 minutes for immediate actions)
  - Focus on truly immediate, actionable steps (not strategic processes)
  - Avoid confusion with longer-term strategic initiatives
  - Reserved only for low-risk activities that can be implemented immediately

#### Chapter 3 Refinements
- FDO narrative accuracy improved
- Clarified initial broad technology focus
- Machine learning focus from 41st term properly documented
- SECIモデルは「無意識の実践」ではなく「意図的な採用」（2020年設立時から）
- "Learning-as-a-Service" → "「育てて返す」モデル" throughout

#### Chapter 4 Comprehensive Revision
- Added ESM AI utilization history timeline (2023-2025)
- Integrated story of late Professor Nonaka's SECI model and AI insights
- Emphasized "tacit knowledge → tacit knowledge" as Eiwa's competitive advantage
- Restructured SECI model explanations to eliminate redundancy
- Changed section names for better impact:
  - "体験談" → "個人から組織へ：AI活用の変革ストーリー"
  - "活用事例" → "実践知を育む組織設計：SECIモデルとフロネシス"
- Enhanced narrative flow from individual AI adoption to organizational capability

#### Chapter 5-7 and Epilogue Refinements (December 2025)
- Applied Okajima style guide across all chapters for consistency
- **Chapter 5**: OKR and measurement traps, based on 2000万円 project experience
- **Chapter 6**: Japanese enterprise agile transformation, 竹とんぼ型スパイラルアップモデル
- **Chapter 7**: Scaling organizational design, CoE and external communication strategies
- **Epilogue**: Closing narrative connecting all chapters, encouraging reader's own transformation journey

#### Okajima Style Guide Application
- Consistent formatting for headers, lists, and emphasis
- Standardized use of Japanese punctuation and spacing
- Unified approach to figure references (【図表 N-X】format)
- Removed figure number titles from images (pic2-1 to pic7-5)
