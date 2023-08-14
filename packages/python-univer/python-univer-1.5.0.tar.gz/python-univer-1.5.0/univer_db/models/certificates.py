from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime, String, Boolean
from sqlalchemy.orm import relationship

from univer_db.orm import get_base

Base = get_base()


class CertificateType(Base):
    """Тип сертификата"""
    __tablename__ = 'univer_certificate_type'

    # Идентификатор
    id = Column('certificate_type_id', Integer, primary_key=True)

    # Наименование
    name_ru = Column('certificate_type_name_ru', Unicode(200))
    name_kk = Column('certificate_type_name_kz', Unicode(200))
    name_en = Column('certificate_type_name_en', Unicode(200))

    # Статус
    status = Column(Integer)

    def __repr__(self):
        return f'<CertificateType {self} (id={self.id} status={self.status})>'

    def __str__(self):
        return self.name_ru


class Certificate(Base):
    """Сертификат"""
    __tablename__ = 'univer_certificates'

    # Идентификатор
    id = Column('certificate_id', Integer, primary_key=True)

    # Тип сертификата
    type_id = Column('certificate_type_id', ForeignKey('univer_certificate_type.certificate_type_id'))
    type = relationship(CertificateType)

    # Дата получения
    receive_date = Column('certificate_resive_date', DateTime)

    # Номер сертификата
    number = Column('certificate_number', String(50))

    # Общая оценка
    total_mark = Column('certificate_total_mark', Integer)

    # Студент
    student_id = Column('students_id', ForeignKey('univer_students.students_id'))
    student = relationship('Student')

    # Серия
    series = Column('certificate_series', String(10))

    def __repr__(self):
        return f'<Certificate {self} (id={self.id} type_id={self.type_id} student_id={self.student_id})>'

    def __str__(self):
        return f'{self.student}: {self.series}{self.number} ({self.type})'


class CertificateSubject(Base):
    """Дисциплина в сертификате"""
    __tablename__ = 'univer_certificate_subject'

    # Идентификатор
    id = Column('certificate_subject_id', Integer, primary_key=True)

    # Академический степень
    stage_id = Column(ForeignKey('univer_stage.stage_id'))
    stage = relationship('Stage')

    # Статус
    status = Column(Integer)

    # Наименование дисциплины
    name_ru = Column('certificate_subject_name_ru', Unicode(100))
    name_kk = Column('certificate_subject_name_kz', Unicode(100))
    name_en = Column('certificate_subject_name_en', Unicode(100))

    # Дисциплина по-умолчанию
    is_default = Column('certificate_subject_default', Boolean, default=False)

    # Максимальное и минимальное значение
    max_points = Column('maxPoints', Integer)
    min_points = Column('minPoints', Integer)

    # Идентификатор типа дисциплины
    subject_type_id = Column('subjectTypeId', Integer)

    # Год ЕНТ
    ent_pass_year = Column('entPassYear', Integer)

    # Неизвестное поле
    consider_creative_professions = Column('considerCreativeProfessions', Integer)

    # Неизвестное поле
    creative_exam = Column('creativeExam', Integer)

    # Неизвестное поле
    operation = Column(Integer)

    def __repr__(self):
        return f'<CertificateSubject {self} (id={self.id} stage_id={self.stage_id} status={self.status})>'

    def __str__(self):
        return self.name_ru


class CertificatePoint(Base):
    """Оценка в сертификате"""
    __tablename__ = 'univer_certificate_points'

    # Идентификатор
    id = Column('point_id', Integer, primary_key=True)

    # Дисциплина
    subject_id = Column('certificate_subject_id', ForeignKey('univer_certificate_subject.certificate_subject_id'))
    subject = relationship(CertificateSubject)

    # Сертификат
    certificate_id = Column(ForeignKey('univer_certificates.certificate_id'))
    certificate = relationship(Certificate)

    # Значение
    point_value = Column(Integer)

    # Неизвестное поле
    point_traditional_value = Column(String(10))

    def __repr__(self):
        return f'<CertificatePoint {self} (id={self.id} subject_id={self.subject_id} certificate_id={self.certificate_id})>'

    def __str__(self):
        return f'{self.certificate} - {self.subject}: {self.point_value}'
