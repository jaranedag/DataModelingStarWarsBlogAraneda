import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
    correo = Column(String(250))
    contraseña = Column(String(250))

class DetallesPersonajes(Base):
    __tablename__ = 'detalles_personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    especie = Column(String(250))

class DetallesPlanetas(Base):
    __tablename__ = 'detalles_planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    habitabilidad = Column(String(250))
    habitantes = Column(Integer)

class PersonajesFavoritos(Base):
    __tablename__ = 'personajes_favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('detalles_personajes.id'))
    fecha_agregado = Column(DateTime)
    relacion_personaje = relationship("DetallesPersonajes")
    relacion_usuario = relationship("Usuario")

class PlanetasFavoritos(Base):
    __tablename__ = 'planetas_favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('detalles_planetas.id'))
    fecha_agregado = Column(DateTime)
    relacion_planetas = relationship("DetallesPlanetas")
    relacion_usuario = relationship("Usuario")



    """
 class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
"""
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
