# Mert KÜÇÜK - Tanıtım Websitesi Spec

## 1. Project Overview
- **Project Name**: Mert KÜÇÜK Yazılımcı Tanıtım Sitesi
- **Type**: Single-page promotional website
- **Core Functionality**: Kişisel marka tanıtımı, hizmetler ve iletişim
- **Target Users**: Potansiyel müşteriler, iş ortakları

## 2. UI/UX Specification

### Layout Structure
- **Header**: Fixed navigation bar
- **Hero Section**: Full viewport intro with animated text
- **About Section**: Kişisel bilgi ve yetenekler
- **Services Section**: Sunulan hizmetler (3 kart)
- **Portfolio Section**: Proje galerisi
- **Contact Section**: İletişim formu ve bilgiler
- **Footer**: Sosyal medya ve telif

### Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

### Visual Design

#### Color Palette
- **Primary (Navy Blue)**: #1a237e
- **Primary Dark**: #0d1642
- **Secondary (Purple)**: #7c4dff
- **Secondary Light**: #b47cff
- **Accent**: #00e5ff
- **Background Dark**: #0a0a1a
- **Background**: #12122a
- **Text Primary**: #ffffff
- **Text Secondary**: #b8b8d1

#### Typography
- **Headings**: 'Outfit', sans-serif (Google Fonts)
- **Body**: 'DM Sans', sans-serif (Google Fonts)
- **Hero Title**: 4rem (desktop), 2.5rem (mobile)
- **Section Titles**: 2.5rem
- **Body Text**: 1rem

#### Spacing System
- Section padding: 100px vertical
- Container max-width: 1200px
- Card gap: 30px
- Element spacing: 20px

#### Visual Effects
- Glassmorphism cards (backdrop-filter: blur)
- Gradient borders
- Smooth hover transitions (0.3s ease)
- Floating animation for hero elements
- Staggered reveal animations on scroll

### Components

#### Navigation
- Logo (Mert KÜÇÜK text)
- Menu items: Ana Sayfa, Hakkımda, Hizmetler, İletişim
- Transparent background, blur on scroll

#### Hero Section
- Animated gradient background
- Large title with gradient text
- Subtitle with typing effect
- CTA button with glow effect

#### Service Cards
- Icon (using emoji or simple shapes)
- Title
- Description
- Hover: lift and glow

#### Portfolio Grid
- Image cards with overlay
- Hover: scale and show details

#### Contact Form
- Name input
- Email input
- Message textarea
- Submit button with loading state

## 3. Functionality Specification

### Core Features
- Smooth scroll navigation
- Scroll-triggered animations
- Form validation (basic)
- Responsive images
- Social media links

### User Interactions
- Navigation click → smooth scroll to section
- Card hover → lift and glow effect
- Button hover → color shift and scale
- Form submit → validation feedback

### Animations
- Hero: floating shapes, gradient shift
- Sections: fade-in on scroll
- Cards: stagger animation
- Buttons: pulse glow on hover

## 4. Acceptance Criteria
- [x] Page loads without errors
- [x] All sections visible and properly styled
- [x] Navigation works correctly
- [x] Responsive on all devices
- [x] Color scheme matches spec (navy blue + purple)
- [x] Animations are smooth
- [x] Form is functional (client-side)
