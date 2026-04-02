# Design System Document: The Editorial Educator

## 1. Overview & Creative North Star

### Creative North Star: "The Digital Curator"
This design system is built to move beyond the rigid, "boxed-in" feel of traditional educational software. It adopts a high-end editorial aesthetic that balances professional authority with an approachable, illustrative soul. We reject the "standard template" look in favor of an expansive layout that uses generous whitespace as a primary design element rather than a secondary consideration.

The system breaks the mold through:
*   **Intentional Asymmetry:** Overlapping illustrative elements with structured text to create a sense of motion.
*   **Editorial Scale:** Using high-contrast typography sizes to lead the eye through a narrative, not just a list of features.
*   **Layered Depth:** Moving away from borders and lines toward a world of tonal shifts and soft, ambient surfaces.

---

## 2. Colors

The color strategy focuses on a sophisticated "Warm Neutral" foundation interrupted by vibrant, high-intent action colors.

### The Foundation
*   **Surface:** `#fcf9f8` (The primary canvas, mimicking premium paper).
*   **Surface-Container-Low:** `#f6f3f2` (Used for subtle sectioning).
*   **Surface-Container-Highest:** `#e4e2e1` (For nested functional areas).

### High-Intent Accents
*   **Primary:** `#0059bb` (The "Trust" blue; used for authority and core navigation).
*   **Secondary:** `#006d3f` (The "Growth" green; used for success states and primary calls to action).
*   **Tertiary:** `#69537d` (The "Intellect" purple; used for secondary emphasis and illustrative highlights).

### Core Philosophy
*   **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. Boundaries must be defined solely through background color shifts. A `surface-container-low` section should simply sit on the `surface` background to define its territory.
*   **Surface Hierarchy & Nesting:** Treat the UI as stacked sheets of fine paper. Use `surface-container-lowest` for cards sitting on a `surface-container-low` background to create natural, soft depth.
*   **The "Glass & Gradient" Rule:** To provide visual "soul," use subtle linear gradients (Primary to Primary-Container) for hero backgrounds. For floating utility panels, utilize Glassmorphism with a `backdrop-filter: blur(12px)` and a semi-transparent `surface` color.

---

## 3. Typography

The system utilizes **Plus Jakarta Sans** (interpreting the modern spirit of Figtree) to create a clean, geometric, yet friendly reading experience.

*   **Display (lg/md):** Used for "Hook" statements. Set with tight letter-spacing (-0.02em) to feel like a high-end magazine header.
*   **Headline (lg/md):** Defined as the "Narrative" level. These should be bold and commanding, leading the user into new content chapters.
*   **Body (lg/md):** The "Information" level. Optimized for long-form educational reading with a generous line-height (1.6) to prevent eye fatigue.
*   **Label (md/sm):** Reserved for metadata and technical indicators. These are often set in all-caps with increased letter-spacing (+0.05em) for a "curated" feel.

---

## 4. Elevation & Depth

We move away from the "shadow-heavy" look of Material Design toward a more atmospheric, tonal layering approach.

*   **The Layering Principle:** Depth is achieved by stacking. A `surface-container-lowest` card placed on a `surface-container-low` section creates a sophisticated "lift" without a single drop shadow.
*   **Ambient Shadows:** If a floating element (like a modal) requires a shadow, use an extra-diffused, low-opacity style.
    *   *Spec:* `0 12px 32px rgba(27, 28, 28, 0.06)`. The shadow color is a tinted version of `on-surface`, never a neutral grey.
*   **The "Ghost Border" Fallback:** If accessibility requires a border, use the `outline-variant` token at **15% opacity**. 100% opaque, high-contrast borders are forbidden.
*   **Glassmorphism:** For overlays, use a semi-transparent `surface` (80% alpha) combined with a backdrop blur. This allows the vibrant brand colors to bleed through, making the layout feel integrated.

---

## 5. Components

### Buttons
*   **Primary:** Solid `secondary` (Green) or `primary` (Blue). Large corner radius (`md`: 0.75rem). No shadows; instead, use a subtle `primary-container` hover shift.
*   **Secondary:** Ghost style with a "Ghost Border" (`outline-variant` at 20%) and `primary` text.
*   **Tertiary:** Text-only with an underline that appears on hover, reinforcing the editorial feel.

### Cards
*   **Construction:** Never use dividers. Separate internal content using the **Spacing Scale** (e.g., `8` for vertical padding).
*   **Style:** Use a `surface-container-lowest` background against a `surface` or `surface-container-low` page.

### Chips & Tags
*   **Selection Chips:** Use `tertiary-fixed` background with `on-tertiary-fixed` text for a soft, professional highlight.
*   **Radius:** Always use `full` (9999px) for chips to contrast against the more structured cards.

### Input Fields
*   **Visual Style:** Soft-filled backgrounds (`surface-container-highest`) rather than outlined boxes.
*   **Focus State:** A 2px solid `primary` bottom border only, or a subtle `primary` glow, maintaining the "no-line" aesthetic for the rest of the container.

### Illustrative Accents
*   **Floating Elements:** Distribute hand-drawn illustrative elements across the layout. These should overlap container edges (using negative margins) to break the "grid" and add a human touch.

---

## 6. Do's and Don'ts

### Do:
*   **Do** use asymmetrical margins. If the left margin is `12`, the right margin for an illustrative element can be `0` to bleed off the page.
*   **Do** prioritize the "Warm Neutral" (`#fcf9f8`) as the dominant screen color to keep the experience feeling "educational" and calm.
*   **Do** use `display-lg` typography for single, impactful sentences to create a rhythm change in long pages.

### Don't:
*   **Don't** use 1px dividers to separate list items. Use vertical spacing (`3` or `4` on the scale) and soft background shifts.
*   **Don't** use "pure black" (#000) for text. Use `on-surface` (#1b1c1c) for a softer, more premium contrast.
*   **Don't** cram content. If a section feels crowded, double the white space. The design system thrives on "the luxury of space."
*   **Don't** use standard box-shadows. If it looks like a "default button," it needs more diffusion and less opacity.