from fpdf import FPDF

# Define a custom PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "7-Day Ninja Leg Speed Training Plan", ln=True, align="C")
        self.ln(8)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(4)

    def section_body(self, body):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

# Text content (cleaned of special characters)
def clean(text):
    return text.replace("–", "-").replace("’", "'")

intro = clean("""This 7-day plan focuses on increasing your leg speed, explosiveness, and sprint acceleration.
With full commitment, expect gains in 1 week and peak ninja speed in 2-3 weeks.""")

warmup = clean("""Daily Warm-up (10 min):
- High knees - 3x30 sec
- A-skips - 3x20 meters
- Leg swings (front, side) - 15 reps per leg
- Bounding - 2x15m""")

core_drills = clean("""Core Speed Drills (15–30 min daily):
1. Sprint Starts - 5x10m bursts
2. Tuck Jumps - 3 sets of 10
3. Ladder Drills - Fast feet
4. Fast-Feet Shuffle - 3x30 sec
5. Jump Lunges - 3 sets of 8 per leg""")

recovery = clean("""Recovery & Nutrition:
- Sleep: Minimum 8 hours daily
- Eat: Protein + carbs post-workout
- Stretch: Quads, hamstrings, calves, and hips every night""")

timeline = clean("""Timeline:
- Day 3-5: Feel quicker, lighter
- Day 7: Noticeable leg speed
- Day 14+: Hit ninja-level acceleration""")

hacks = clean("""Pro Ninja Speed Hacks:
- Sprint with resistance bands
- Do uphill sprints for more power
- Barefoot sprint on grass for natural mechanics""")

# Create PDF
pdf = PDF()
pdf.add_page()

pdf.section_title("Introduction")
pdf.section_body(intro)

pdf.section_title("Daily Warm-up")
pdf.section_body(warmup)

pdf.section_title("Core Speed Drills")
pdf.section_body(core_drills)

pdf.section_title("Recovery & Nutrition")
pdf.section_body(recovery)

pdf.section_title("Progress Timeline")
pdf.section_body(timeline)

pdf.section_title("Pro Ninja Speed Hacks")
pdf.section_body(hacks)

# Save PDF
pdf.output("Ninja_Leg_Speed_Training_7_Day_Plan.pdf")

print("✅ PDF generated: Ninja_Leg_Speed_Training_7_Day_Plan.pdf")
