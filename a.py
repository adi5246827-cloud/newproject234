from crewai import Agent, Crew, Task

# יצירת מספר אגנטים
agent1 = Agent(
    role="חוקר",
    goal="לאסוף מידע רלוונטי על נושא מוגדר",
    backstory="חוקר יסודי המתמחה באיסוף מקורות מהימנים.",
)

agent2 = Agent(
    role="כותב",
    goal="לכתוב תקציר או מסמך על סמך המידע שנאסף",
    backstory="כותב מקצועי עם ניסיון ביצירת תוכן ברור ומדויק.",
)

# יצירת משימות עבור כל אגנט
task1 = Task(
    description="אסוף מידע עדכני ממקורות מהימנים בנושא הנתון.",
    expected_output="רשימת עובדות רלוונטיות ומקורות.",
    agent=agent1,
)

task2 = Task(
    description="כתוב תקציר באורך קצר על סמך המידע שאסף החוקר.",
    expected_output="פסקה מסכמת וברורה.",
    agent=agent2,
)

# הגדרת הצוות והפעלתו
crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    verbose=True
)

# הפעלת המולטי-אג'נט בפועל
result = crew.kickoff()
print(result)