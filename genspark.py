import random
 
class GenAIAgent:
    def reason(self, input_data, context="General"):
        return f"[GenAI reasoning applied in {context} context: {input_data}]"
 
class ProfileAnalysisAgent(GenAIAgent):
    def analyze_profile(self, employee):
        print(f"Analyzing profile for {employee['name']}...")
        # Enhanced reasoning for skill-based level inference
        level = "Intermediate" if len(employee['skills']) > 2 else "Beginner"
        reasoning = f"Inferred level '{level}' based on skills: {employee['skills']} and target role: {employee['target']}"
        print(self.reason(reasoning, context="Profile Analysis"))
        return level
 
class AssessmentAgent(GenAIAgent):
    def run_assessment(self, level):
        print(f"Conducting {level} level assessment...")
        # Simulate a dynamic assessment score
        score = random.randint(50, 95)
        reasoning = f"Generated a score of {score}% for a {level} level assessment."
        print(self.reason(reasoning, context="Assessment"))
        return score
 
class RecommendationAgent(GenAIAgent):
    def recommend(self, profile, score):
        print("Generating personalized course recommendations...")
        # Enhanced recommendations based on score and target role
        if score > 85:
            courses = ["Advanced Angular", "System Design", "Microservices Architecture"]
        elif score > 60:
            courses = ["Angular Basics", "JavaScript Deep Dive", "REST API Development"]
        else:
            courses = ["HTML/CSS Refresher", "Intro to Angular", "Programming Fundamentals"]
        reasoning = f"Recommended courses based on score {score}% and target role '{profile['target']}': {courses}"
        print(self.reason(reasoning, context="Recommendation"))
        return courses
 
class ProgressTrackerAgent(GenAIAgent):
    def track(self, employee, courses):
        completed = random.sample(courses, k=1)
        pending = list(set(courses) - set(completed))
        print(f"Tracking progress for {employee['name']}...")
        reasoning = f"Completed: {completed}, Pending: {pending}"
        print(self.reason(reasoning, context="Progress Tracking"))
        return {"completed": completed, "pending": pending}
 
# Simulated user
employee = {
    "id": "E123",
    "name": "Adam",
    "role": "Learner",
    "skills": ["Spring Boot", "MySQL"],
    "target": "Full Stack Developer"
}
 
# Simulated CLI Workflow
print("=== Personalized Learning CLI (Enhanced GenAI Version) ===")
 
# Instantiate agents
profile_agent = ProfileAnalysisAgent()
assessment_agent = AssessmentAgent()
recommendation_agent = RecommendationAgent()
tracker_agent = ProgressTrackerAgent()
 
# Workflow execution
level = profile_agent.analyze_profile(employee)
score = assessment_agent.run_assessment(level)
courses = recommendation_agent.recommend(employee, score)
progress = tracker_agent.track(employee, courses)
