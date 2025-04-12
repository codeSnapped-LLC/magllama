CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    preferences TEXT,
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE trivy_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE checkov_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE snyk_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE owasp_zap_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE sonarqube_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE grype_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE bandit_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE semgrep_scans (
    id SERIAL PRIMARY KEY,
    scan_date TIMESTAMP,
    result TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP
);
