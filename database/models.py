from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TrivyScan(Base):
    __tablename__ = 'trivy_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)

class CheckovScan(Base):
    __tablename__ = 'checkov_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)

class SnykScan(Base):
    __tablename__ = 'snyk_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)

class OwaspZapScan(Base):
    __tablename__ = 'owasp_zap_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)

class SonarQubeScan(Base):
    __tablename__ = 'sonarqube_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)

class GrypeScan(Base):
    __tablename__ = 'grype_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)

class BanditScan(Base):
    __tablename__ = 'bandit_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)

class SemgrepScan(Base):
    __tablename__ = 'semgrep_scans'
    id = Column(Integer, primary_key=True, index=True)
    scan_date = Column(DateTime)
    result = Column(String)
