# Blog Images Requirements

This directory contains optimized WebP images for the InsureCalcu blog posts.

## Image Specifications

### Hero Images (1200x630px)
- `car-insurance-guide.webp`
- `lower-premium-tips.webp`
- Quality: 80%
- File size target: < 150KB
- Encoding: Lossy

### Content Images (800x450px)
- `liability-coverage.webp`
- `collision-coverage.webp`
- `comprehensive-coverage.webp`
- `pip-coverage.webp`
- `uninsured-coverage.webp`
- `vehicle-choice.webp`
- `smart-habits.webp`
- Quality: 75%
- File size target: < 100KB
- Encoding: Lossy

### Author Avatar (120x120px)
- `author-avatar.webp`
- Quality: 85%
- File size target: < 30KB
- Encoding: Lossy
- Border-radius: 50% (applied via CSS)

## Image Optimization Guidelines

1. Use WebP format for all images
2. Maintain aspect ratios
3. Compress images before deployment
4. Include appropriate alt text in HTML
5. Implement lazy loading for better performance

## Directory Structure
```
static/
└── images/
    ├── car-insurance-guide.webp
    ├── liability-coverage.webp
    ├── collision-coverage.webp
    ├── comprehensive-coverage.webp
    ├── pip-coverage.webp
    ├── uninsured-coverage.webp
    ├── lower-premium-tips.webp
    ├── vehicle-choice.webp
    ├── smart-habits.webp
    └── author-avatar.webp
```
