TIERS_FEATURE_LIMITS = {
    "Free": {
            "credits" : 1000,
            "feature_limits" : {
                                "projects": 1,
                                "environments": 1,
                                "build_minutes": 30,
                                "vcpu_cu": 50,
                                "vmemory_GB": 4,
                                }
        },
    "Pro": {
            "credits" : 10000,
            "feature_limits" : {
                                "projects": 1,
                                "environments": 1,
                                "build_minutes": 30,
                                "vcpu_cu": 50,
                                "vmemory_GB": 4,
                                }
        },
    "Team": {
            "credits" : 50000,
            "feature_limits" : {
                                "projects": 1,
                                "environments": 1,
                                "build_minutes": 30,
                                "vcpu_cu": 50,
                                "vmemory_GB": 4,
                                }
        },
    "Scale": {
            "credits" : 500000,
            "feature_limits" : {
                                "projects": 1,
                                "environments": 1,
                                "build_minutes": 30,
                                "vcpu_cu": 50,
                                "vmemory_GB": 4,
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