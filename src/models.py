from eralchemy2 import render_er
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)

    # Un usuario tiene muchos favoritos
    favorites: Mapped[List["Favorite"]] = relationship(back_populates="user")


class People(db.Model):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[str] = mapped_column(String(20))
    mass: Mapped[str] = mapped_column(String(20))
    hair_color: Mapped[str] = mapped_column(String(50))


class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(50))
    terrain: Mapped[str] = mapped_column(String(50))
    population: Mapped[str] = mapped_column(String(50))


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id: Mapped[int] = mapped_column(primary_key=True)

    # Relación con el Usuario
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="favorites")

    # Relación con Personajes
    people_id: Mapped[int] = mapped_column(
        ForeignKey("people.id"), nullable=True)
    people: Mapped["People"] = relationship()

    # Relación con Planetas
    planet_id: Mapped[int] = mapped_column(
        ForeignKey("planet.id"), nullable=True)
    planet: Mapped["Planet"] = relationship()


if __name__ == "__main__":
    try:
        render_er(db.Model, 'diagram.png')
        print("¡Éxito! El diagrama de Star Wars se ha generado en diagram.png")
    except Exception as e:
        print("Hubo un error al generar el diagrama:")
        print(e)
