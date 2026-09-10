# Localization Rules

## Purpose
These rules guide all translation and localization work across applications.

## Supported Default Languages
- English (`en`) - source language
- French (`fr`) - target language
- Chinese (`zh`, `zh-CN`, or `zh-TW`) - target language depending on the project

## Non-Negotiable Rules
- Do not assume unclear meaning.
- Do not implement until the user clearly authorizes the understood scope.
- Preserve all translation keys.
- Preserve all placeholders exactly.
- Preserve pluralization syntax.
- Preserve HTML, Markdown, and template variables.
- Do not remove comments unless instructed.
- Do not translate internal keys, class names, route names, config names, or code identifiers.
- Do not change application behavior while translating.

## Required Clarifications
Ask the user when:
- Chinese locale is unclear: Simplified Chinese (`zh-CN`) or Traditional Chinese (`zh-TW`).
- The source English text is ambiguous.
- A phrase has business-specific meaning.
- Tone is unclear: formal, friendly, corporate, religious, playful, legal, etc.
- Text contains legal, financial, compliance, religious, or medical meaning.
- Product names, brand names, or technical terms may need to stay untranslated.

## Quality Standard
Translations must be:
- Accurate.
- Natural.
- User-friendly.
- Consistent.
- Production-ready.
- Suitable for web and mobile UI.

## QA Integration
After Ling translates and Ying reviews, Armstrong must validate:
- Language switching.
- Missing text.
- Broken layout from longer translations.
- Mobile responsiveness.
- Form validation messages.
- Emails and notifications.
- Empty states and error states.
