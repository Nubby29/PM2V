# PM2V — Client Request Checklist

## Status Legend
- [x] Done | [ ] TODO | [~] In Progress

| # | Section | Requirement | Status | Notes |
|---|---------|-------------|--------|-------|
| 1 | Global Header | Consistent header design across all internal pages | [x] Done | .global-header CSS applied; topbar pattern on all pages |
| 2 | Global Header | Dynamic date/time (no static date) | [x] Done | setInterval(updateRoleClocks,1000) updates 6 page date IDs |
| 3 | Global Header | Remove unnecessary page subtitles | [x] Done | Dashboard and Reports subtitles removed |
| 4 | Global Header | Consistent spacing/alignment across all pages | [x] Done | Unified .topbar with 30px bottom margin |
| 5 | Sidebar/Nav | Center and size PM2V logo | [x] Done | .logo-wrap 184px centered; .logo 158x158px |
| 6 | Sidebar/Nav | Remove WORKSPACE and ACCOUNT labels | [x] Done | No nav-group-label HTML elements present |
| 7 | Sidebar/Nav | Clean nav items, proper spacing | [x] Done | .nav gap:7px; .nav a height:52px |
| 8 | Sidebar/Nav | Group Profile and Logout under account area | [x] Done | nav-divider separates Profile; Logout in .logout |
| 9 | Sidebar/Nav | Consistent sidebar across all internal pages | [x] Done | Single .sidebar 295px fixed shared everywhere |
| 10 | Dashboard | Remove Welcome back text | [x] Done | Text removed from dashboard section |
| 11 | Dashboard | Make Total Items and Categories cards clickable | [x] Done | .dashboard-stat.cursor-pointer + data-click-page + JS |
| 12 | Dashboard | Center icons, numbers, labels in cards | [x] Done | CSS grid centering; 51x51px icons |
| 13 | Dashboard | Active Items aligned with other stat cards | [x] Done | All 3 cards in .dashboard-stats grid |
| 14 | Dashboard | Dynamic date/time | [x] Done | dashboardDate updated every 1s |
| 15 | Dashboard | Improve spacing and alignment | [x] Done | Consistent padding, margins, grid |
| 16 | Physical Inventory | Add standardized global header | [x] Done | .topbar with #inventoryDate |
| 17 | Physical Inventory | Improve Items/Total Weight summary layout | [x] Done | inventorySummaryCount and inventorySummaryWeight |
| 18 | Physical Inventory | Spacing between summary, filters, scanner, table | [x] Done | Proper section margins |
| 19 | Physical Inventory | Consistent logo/navigation with Dashboard | [x] Done | Shared sidebar |
| 20 | Reports | Add standardized global header | [x] Done | .topbar with #reportsDate |
| 21 | Reports | Remove Business intelligence subtitle | [x] Done | Subtitle not present |
| 22 | Reports | Remove Export PDF | [x] Done | No Export PDF button present |
| 23 | Reports | Clickable stat cards | [x] Done | .report-kpi-card.cursor-pointer + JS |
| 24 | Reports | Clickable Stock Status cards | [x] Done | .stock-status-card.cursor-pointer + JS |
| 25 | Reports | Expandable/collapsible Report Filters | [ ] TODO | CSS defined but not applied to HTML |
| 26 | Reports | More space and improved filter layout | [x] Done | Category, Status, Period dropdowns + Reset |
| 27 | Reports | Remove unnecessary reports/analytics | [x] Done | Kept business-relevant reports only |
| 28 | Reports | Use business-relevant terminology | [x] Done | Inventory records, target stock range, etc. |
| 29 | Profile | Add standardized global header | [x] Done | .topbar with #profileDate |
| 30 | Profile | Dynamic date/time | [x] Done | profileDate updated every 1s |
| 31 | Profile | Reduce excessive empty space | [x] Done | Compact layout |
| 32 | Profile | Improve spacing between info sections | [x] Done | Consistent card padding |
| 33 | Profile | Fix Member Since / Activity Info display | [x] Done | Dynamic date; activity rendered |
| 34 | Profile | Edit Profile, Change Password, Logout aligned | [x] Done | .profile-actions flex layout |
| 35 | AI Scrap Classifier | Clean, understandable interface | [x] Done | Upload/Scan/Camera buttons, clear results |
| 36 | AI Scrap Classifier | Show AI model being used | [x] Done | AI_CONFIG workflow name visible |
| 37 | AI Scrap Classifier | Confidence from AI result, not hardcoded | [x] Done | normalizeResult parses confidence from API |
| 38 | AI Scrap Classifier | Reliable classification via AI workflow | [x] Done | callAIWorkflow uses Render proxy |
| 39 | AI Scrap Classifier | Distinguish all result fields | [x] Done | Separate elements for each field |
| 40 | AI Scrap Classifier | Use Result transfers data correctly | [x] Done | ai.apply sets name, category, condition |
| 41 | AI Scrap Classifier | Remove technical/debug text | [x] Done | Clean user-facing text |
| 42 | Landing Page | Improve PM2V logo presentation | [x] Done | .pm2v-landing-logo-large in hero |
| 43 | Landing Page | Green-and-white branding | [x] Done | Green buttons, white text, gradients |
| 44 | Landing Page | Login CTA prominent | [x] Done | Hero + CTA section login buttons |
| 45 | Landing Page | Improve About Us section | [x] Done | 4 feature cards |
| 46 | Landing Page | Improve FAQs section | [x] Done | FAQ accordion |
| 47 | Landing Page | Polished, professional look | [x] Done | Consistent styling throughout |
| 48 | User Management | Improve layout and spacing | [x] Done | Table with proper margins |
| 49 | User Management | Consistent header | [x] Done | .topbar with #usersDate |
| 50 | User Management | Clear and functional actions | [x] Done | Approve/Reject buttons, role badges |
| 51 | User Management | Improve user info presentation | [x] Done | Name, email, role, status columns |
| 52 | User Management | Remove unnecessary elements | [x] Done | Focused on admin functions |
| 53 | Footer | Clean, centered footer on all pages | [~] Partial | Landing has footer; internal pages need .global-footer added |
| 54 | Overall | Do NOT redesign from scratch | [x] Done | Existing structure preserved |
| 55 | Overall | Maintain green/white branding | [x] Done | Consistent colors throughout |
| 56 | Overall | Unified system feel | [x] Done | Shared sidebar, topbar, card styles |
| 57 | Overall | Fix excessive empty spaces | [x] Done | Compact layouts applied |
| 58 | Overall | Fix inconsistent margins/padding/alignment | [x] Done | Consistent CSS classes |
| 59 | Overall | Remove unnecessary text/labels/sections | [x] Done | Labels and subtitles removed |
| 60 | Overall | Interactive summary cards where indicated | [x] Done | All targeted cards clickable |
| 61 | Overall | Dynamic dates/times/counts/statistics | [x] Done | setInterval + Firestore data |
| 62 | Overall | Prioritize business-relevant info | [x] Done | Business terminology used |
| 63 | Overall | Clean, professional, capstone-ready | [x] Done | Polished unified design |
