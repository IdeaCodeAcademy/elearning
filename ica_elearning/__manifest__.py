{
    "name": "ICA E-Learning",
    "author": "IdeaCode Academy",
    "category": "eLearning",
    "depends": ["base", "web","report_xlsx"],
    "data": [
        "report/ica_course_report_action.xml",
        "report/course_enrollment_report.xml",

        "data/ica_course_sequence.xml",

        "security/security.xml",
        "security/ir.model.access.csv",
        "wizard/ica_course_feedback_wizard.xml",
        "views/ica_course.xml",
        "views/ica_course_module.xml",
        "views/ica_course_lesson.xml",
        "views/ica_course_enrollment.xml",
        "views/ica_course_feedback.xml",
        "views/menus.xml",

    ],
    "demo": [
        "demo/ica_course.xml",
    ],
    "license": "LGPL-3"
}
