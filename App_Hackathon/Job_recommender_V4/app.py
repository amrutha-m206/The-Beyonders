from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

JOBS = [
    # Technical Jobs - Programming (10+ jobs)
    {
        "id": 1,
        "title": "Senior Software Engineer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Develop scalable web applications using Python and cloud technologies",
        "skills": ["python", "aws", "django", "kubernetes"],
        "location": "San Francisco, CA",
        "salary_range": "$120,000 - $150,000"
    },
    {
        "id": 2,
        "title": "Backend Python Developer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Design and implement complex backend systems for enterprise applications",
        "skills": ["python", "django", "postgresql", "microservices"],
        "location": "Boston, MA",
        "salary_range": "$110,000 - $140,000"
    },
    {
        "id": 3,
        "title": "Java Enterprise Architect",
        "category": "technical",
        "subcategory": "programming",
        "description": "Lead design of large-scale enterprise Java applications",
        "skills": ["java", "spring boot", "microservices", "cloud architecture"],
        "location": "New York, NY",
        "salary_range": "$140,000 - $180,000"
    },
    {
        "id": 4,
        "title": "Embedded Systems Engineer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Develop low-level software for IoT and embedded devices",
        "skills": ["c++", "embedded systems", "iot", "rust"],
        "location": "Austin, TX",
        "salary_range": "$100,000 - $130,000"
    },
    {
        "id": 5,
        "title": "Blockchain Developer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Create smart contracts and blockchain solutions",
        "skills": ["solidity", "ethereum", "blockchain", "python"],
        "location": "San Jose, CA",
        "salary_range": "$130,000 - $160,000"
    },
    {
        "id": 6,
        "title": "Game Software Engineer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Develop game mechanics and optimize game performance",
        "skills": ["c++", "unity", "game development", "opengl"],
        "location": "Seattle, WA",
        "salary_range": "$110,000 - $145,000"
    },
    {
        "id": 7,
        "title": "Mobile Game Developer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Create engaging mobile game experiences for iOS and Android",
        "skills": ["swift", "kotlin", "unity", "game design"],
        "location": "Los Angeles, CA",
        "salary_range": "$95,000 - $125,000"
    },
    {
        "id": 8,
        "title": "Systems Programmer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Develop low-level system software and optimize system performance",
        "skills": ["c", "linux", "kernel development", "system architecture"],
        "location": "Chicago, IL",
        "salary_range": "$115,000 - $150,000"
    },
    {
        "id": 9,
        "title": "Robotics Software Engineer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Design and implement software for robotic systems",
        "skills": ["python", "ros", "machine learning", "computer vision"],
        "location": "Pittsburgh, PA",
        "salary_range": "$120,000 - $155,000"
    },
    {
        "id": 10,
        "title": "Quantum Computing Developer",
        "category": "technical",
        "subcategory": "programming",
        "description": "Research and develop quantum computing algorithms",
        "skills": ["python", "quantum computing", "linear algebra", "machine learning"],
        "location": "Remote",
        "salary_range": "$130,000 - $170,000"
    },

    # Technical Jobs - Web Development (10+ jobs)
    {
        "id": 11,
        "title": "Full Stack Web Developer",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Build responsive and scalable web applications",
        "skills": ["javascript", "react", "nodejs", "html", "css"],
        "location": "Remote",
        "salary_range": "$90,000 - $130,000"
    },
    {
        "id": 12,
        "title": "React Frontend Engineer",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Create modern, interactive user interfaces",
        "skills": ["react", "typescript", "redux", "graphql"],
        "location": "San Francisco, CA",
        "salary_range": "$110,000 - $145,000"
    },
    {
        "id": 13,
        "title": "Angular Developer",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Develop enterprise-level web applications",
        "skills": ["angular", "typescript", "rxjs", "node.js"],
        "location": "New York, NY",
        "salary_range": "$100,000 - $135,000"
    },
    {
        "id": 14,
        "title": "Vue.js Specialist",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Build dynamic and responsive single-page applications",
        "skills": ["vue.js", "nuxt.js", "vuex", "typescript"],
        "location": "Austin, TX",
        "salary_range": "$95,000 - $125,000"
    },
    {
        "id": 15,
        "title": "WordPress Developer",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Create custom WordPress themes and plugins",
        "skills": ["php", "wordpress", "javascript", "woocommerce"],
        "location": "Denver, CO",
        "salary_range": "$80,000 - $110,000"
    },
    {
        "id": 16,
        "title": "WebGL Graphics Developer",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Create interactive 3D web experiences",
        "skills": ["webgl", "three.js", "javascript", "css3d"],
        "location": "Seattle, WA",
        "salary_range": "$105,000 - $140,000"
    },
    {
        "id": 17,
        "title": "Progressive Web App Specialist",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Develop high-performance progressive web applications",
        "skills": ["pwa", "service workers", "web performance", "react"],
        "location": "Boston, MA",
        "salary_range": "$95,000 - $130,000"
    },
    {
        "id": 18,
        "title": "E-commerce Web Developer",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Build and optimize online shopping platforms",
        "skills": ["javascript", "shopify", "stripe", "payment integration"],
        "location": "Chicago, IL",
        "salary_range": "$85,000 - $120,000"
    },
    {
        "id": 19,
        "title": "Headless CMS Developer",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Implement modern headless content management systems",
        "skills": ["jamstack", "gatsby", "contentful", "netlify"],
        "location": "Portland, OR",
        "salary_range": "$100,000 - $135,000"
    },
    {
        "id": 20,
        "title": "Serverless Web Architect",
        "category": "technical",
        "subcategory": "web_development",
        "description": "Design scalable serverless web architectures",
        "skills": ["aws lambda", "serverless", "nodejs", "api gateway"],
        "location": "Remote",
        "salary_range": "$115,000 - $150,000"
    },

    {
    "id": 21,
    "title": "Machine Learning Engineer",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Develop advanced machine learning models for predictive analytics",
    "skills": ["python", "machine learning", "tensorflow", "deep learning", "neural networks"],
    "location": "San Francisco, CA",
    "salary_range": "$130,000 - $170,000"
},
{
    "id": 22,
    "title": "AI Research Scientist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Conduct cutting-edge research in artificial intelligence and machine learning",
    "skills": ["deep learning", "nlp", "python", "pytorch", "research methodology"],
    "location": "Boston, MA",
    "salary_range": "$140,000 - $180,000"
},
{
    "id": 23,
    "title": "Big Data Architect",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Design and implement large-scale data processing systems",
    "skills": ["hadoop", "spark", "scala", "big data", "data warehousing"],
    "location": "New York, NY",
    "salary_range": "$125,000 - $160,000"
},
{
    "id": 24,
    "title": "Predictive Analytics Specialist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Create predictive models to drive business decision-making",
    "skills": ["r", "statistical analysis", "machine learning", "tableau", "predictive modeling"],
    "location": "Chicago, IL",
    "salary_range": "$110,000 - $145,000"
},
{
    "id": 25,
    "title": "Computer Vision Engineer",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Develop advanced image and video recognition algorithms",
    "skills": ["opencv", "python", "deep learning", "image processing", "tensorflow"],
    "location": "Seattle, WA",
    "salary_range": "$120,000 - $155,000"
},
{
    "id": 26,
    "title": "Natural Language Processing Researcher",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Build advanced NLP models for text analysis and generation",
    "skills": ["nlp", "transformer models", "hugging face", "python", "machine learning"],
    "location": "Remote",
    "salary_range": "$135,000 - $175,000"
},
{
    "id": 27,
    "title": "Genomic Data Scientist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Analyze genetic data to support medical research and personalized medicine",
    "skills": ["bioinformatics", "r", "python", "statistical analysis", "genomic data"],
    "location": "San Diego, CA",
    "salary_range": "$115,000 - $150,000"
},
{
    "id": 28,
    "title": "Data Science Consultant",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Provide strategic data science solutions to enterprise clients",
    "skills": ["machine learning", "business intelligence", "tableau", "sql", "communication"],
    "location": "Washington, D.C.",
    "salary_range": "$120,000 - $160,000"
},
{
    "id": 29,
    "title": "Recommender Systems Engineer",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Design personalized recommendation algorithms for digital platforms",
    "skills": ["machine learning", "collaborative filtering", "python", "data mining", "a/b testing"],
    "location": "Austin, TX",
    "salary_range": "$110,000 - $145,000"
},
{
    "id": 30,
    "title": "Climate Data Scientist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Analyze environmental data to support climate change research",
    "skills": ["python", "climate modeling", "statistical analysis", "data visualization", "r"],
    "location": "Boulder, CO",
    "salary_range": "$105,000 - $140,000"
},
{
    "id": 31,
    "title": "Healthcare Analytics Specialist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Develop predictive models for healthcare outcomes and resource allocation",
    "skills": ["healthcare analytics", "machine learning", "hipaa", "sql", "tableau"],
    "location": "Boston, MA",
    "salary_range": "$115,000 - $150,000"
},
{
    "id": 32,
    "title": "Financial Risk Modeling Data Scientist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Create advanced risk assessment models for financial institutions",
    "skills": ["financial modeling", "machine learning", "python", "risk analysis", "statistical modeling"],
    "location": "New York, NY",
    "salary_range": "$130,000 - $170,000"
},
{
    "id": 33,
    "title": "E-commerce Optimization Data Scientist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Optimize online retail performance through advanced data analysis",
    "skills": ["machine learning", "customer segmentation", "a/b testing", "python", "sql"],
    "location": "San Francisco, CA",
    "salary_range": "$115,000 - $150,000"
},
{
    "id": 34,
    "title": "Robotics Data Scientist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Develop machine learning algorithms for robotic systems and automation",
    "skills": ["machine learning", "robotics", "python", "computer vision", "sensor data analysis"],
    "location": "Pittsburgh, PA",
    "salary_range": "$125,000 - $160,000"
},
{
    "id": 35,
    "title": "Sports Analytics Data Scientist",
    "category": "technical",
    "subcategory": "data_science",
    "description": "Apply advanced analytics to improve athletic performance and team strategies",
    "skills": ["sports analytics", "machine learning", "python", "data visualization", "statistical modeling"],
    "location": "Chicago, IL",
    "salary_range": "$100,000 - $135,000"
},

# Business - Marketing Jobs (15+ jobs)
{
    "id": 36,
    "title": "Digital Marketing Strategist",
    "category": "business",
    "subcategory": "marketing",
    "description": "Develop comprehensive digital marketing strategies for global brands",
    "skills": ["digital marketing", "social media marketing", "google analytics", "content strategy"],
    "location": "New York, NY",
    "salary_range": "$85,000 - $120,000"
},
{
    "id": 37,
    "title": "Growth Marketing Manager",
    "category": "business",
    "subcategory": "marketing",
    "description": "Drive user acquisition and retention through innovative marketing techniques",
    "skills": ["growth hacking", "a/b testing", "conversion optimization", "analytics"],
    "location": "San Francisco, CA",
    "salary_range": "$100,000 - $140,000"
},
{
    "id": 38,
    "title": "Social Media Marketing Specialist",
    "category": "business",
    "subcategory": "marketing",
    "description": "Create and manage engaging social media campaigns across platforms",
    "skills": ["social media marketing", "content creation", "community management", "analytics"],
    "location": "Los Angeles, CA",
    "salary_range": "$65,000 - $95,000"
},
{
    "id": 39,
    "title": "SEO Expert",
    "category": "business",
    "subcategory": "marketing",
    "description": "Optimize website performance and search engine rankings",
    "skills": ["seo", "google analytics", "keyword research", "content strategy"],
    "location": "Austin, TX",
    "salary_range": "$75,000 - $110,000"
},
{
    "id": 40,
    "title": "Content Marketing Manager",
    "category": "business",
    "subcategory": "marketing",
    "description": "Develop and execute content marketing strategies",
    "skills": ["content marketing", "copywriting", "content strategy", "seo"],
    "location": "Chicago, IL",
    "salary_range": "$80,000 - $115,000"
}


]

@app.route('/')
def home():
    return render_template('index.html', jobs=JOBS)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_skills = data.get('skills', '').lower().split(', ')
    category = data.get('category', '')
    location = data.get('location', '')

    # Recommendation logic
    recommendations = [
        job for job in JOBS 
        if (not category or job['category'] == category) and
           (not location or location.lower() in job['location'].lower()) and
           all(skill in [s.lower() for s in job['skills']] for skill in user_skills if skill)
    ]

    return jsonify(recommendations)

@app.route('/categories')
def get_categories():
    categories = {
        "technical": {
            "programming": ["python", "java", "javascript", "c++", "ruby", "php", "swift", "kotlin"],
            "web_development": ["html", "css", "react", "angular", "vue", "nodejs", "django", "flask"],
            "data_science": ["machine learning", "deep learning", "statistics", "r", "pandas", "numpy"],
            "database": ["sql", "mongodb", "postgresql", "mysql", "oracle"],
            "devops": ["aws", "docker", "kubernetes", "jenkins", "gitlab"]
        },
        "business": {
            "marketing": ["digital marketing", "seo", "social media", "content marketing", "analytics"],
            "finance": ["financial analysis", "accounting", "excel", "financial modeling", "bloomberg"],
            "sales": ["sales strategy", "negotiation", "crm", "salesforce", "lead generation"],
            "management": ["project management", "agile", "scrum", "team leadership", "stakeholder management"]
        },
        "creative": {
            "design": ["ui/ux", "photoshop", "illustrator", "figma", "sketch"],
            "content": ["copywriting", "content strategy", "editing", "storytelling"],
            "multimedia": ["video editing", "animation", "adobe creative suite"]
        }
    }
    return jsonify(categories)

if __name__ == '__main__':
    app.run(debug=True)