TIERS_FEATURE_LIMITS = {
    "Free": {
            "credits" : 1000,
            "feature_limits" : {
                                "projects": 1,
                                "environments": 1,
                                "build_minutes": 30,
                                "vcpu_cu": 1,
                                "vmemory_GB": 2,
                                }
        },
    "Pro": {
            "credits" : 10000,
            "feature_limits" : {
                                "projects": 5,
                                "environments": 5,
                                "build_minutes": 300,
                                "vcpu_cu": 2,
                                "vmemory_GB": 10,
                                }
        },
    "Team": {
            "credits" : 50000,
            "feature_limits" : {
                                "projects": 15,
                                "environments": 15,
                                "build_minutes": 1200,
                                "vcpu_cu": 5,
                                "vmemory_GB": 10,
                                }
        },
    "Scale": {
            "credits" : 500000,
            "feature_limits" : {
                                "projects": 1000,
                                "environments": 1000,
                                "build_minutes": 300000,
                                "vcpu_cu": 50,
                                "vmemory_GB": 1000,
                                }
        },
    
}

CREDITS_PER_FEATURES = {
    "projects": 100,
    "environments": 100,
    "build_minutes": 5,
    "vcpu_cu": 1,
    "vmemory_GB": 2,
}

SAMPLE_INPUT = {
    "projects" : 1,
    "environments" : 2,
    "build_minutes" : 50,
    "vcpu_cu" : 50,
    "vmemory_GB" : 2,
}