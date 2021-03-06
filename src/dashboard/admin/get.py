from sqlalchemy import text
from ...db import *


def permissions_get(sql=""):
    q = session.query(Permission)
    if not sql == "":
        q = session.query(Permission).filter(text(sql))
    l = q.all()
    return {
        "body": l,
        "query": q
    }


def countries_get(sql=""):
    q = session.query(Country)
    if not sql == "":
        q = session.query(Country).filter(text(sql))
    l = q.all()
    return {
        "body": l,
        "query": q
    }


def cities_get(sql=""):
    q = session.query(City)
    if not sql == "":
        q = session.query(City).filter(text(sql))
    l = q.all()
    bonus = {
        'Country': {}
    }
    for city in l:
        bonus["Country"][city.id] = session.query(Country).filter(
            Country.id == city.country
        ).one().name
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def users_get(sql=""):
    q = session.query(User)
    if not sql == "":
        q = session.query(User).filter(text(sql))
    l = q.all()
    bonus = {
        'City': {},
        'Country': {},
        'Permission': {}
    }
    for user in l:
        bonus["City"][user.id] = session.query(City).filter(
            City.id == user.city
        ).one().name
        bonus["Country"][user.id] = session.query(Country).filter(
            Country.id == user.country
        ).one().name
        bonus["Permission"][user.id] = session.query(Permission).filter(
            Permission.id == user.permission
        ).one().name
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def passwordrecover_get(sql=""):
    q = session.query(PasswordRecover)
    if not sql == "":
        q = session.query(PasswordRecover).filter(text(sql))
    l = q.all()
    bonus = {
        'User': {}
    }
    for token in l:
        bonus["User"][token.id] = session.query(User).filter(
            User.id == token.user
        ).one().username
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def authtokens_get(sql=""):
    q = session.query(AuthToken)
    if not sql == "":
        q = session.query(AuthToken).filter(text(sql))
    l = q.all()
    bonus = {
        'User': {}
    }
    for token in l:
        bonus["User"][token.id] = session.query(User).filter(
            User.id == token.user
        ).one().username
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def payments_get(sql=""):
    q = session.query(Payment)
    if not sql == "":
        q = session.query(Payment).filter(text(sql))
    l = q.all()
    bonus = {
        'FromUser': {},
        'ToUser': {},
    }
    for payment in l:
        bonus["FromUser"][payment.id] = session.query(User).filter(
            User.id == payment.fromUser
        ).one().username
        bonus["ToUser"][payment.id] = session.query(User).filter(
            User.id == payment.toUser
        ).one().username
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def reports_get(sql=""):
    q = session.query(Report)
    if not sql == "":
        q = session.query(Report).filter(text(sql))
    l = q.all()
    bonus = {
        'Reporter': {}
    }
    for report in l:
        bonus["Reporter"][report.id] = session.query(User).filter(
            User.id == report.reporter
        ).one().username
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def messages_get(sql=""):
    q = session.query(Message)
    if not sql == "":
        q = session.query(Message).filter(text(sql))
    l = q.all()
    bonus = {
        'User': {}
    }
    for message in l:
        bonus["User"][message.id] = session.query(User).filter(
            User.id == message.reporter
        ).one().username
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def wallets_get(sql=""):
    q = session.query(Wallet)
    if not sql == "":
        q = session.query(Wallet).filter(text(sql))
    l = q.all()
    bonus = {
        'Owner': {}
    }
    for wallet in l:
        bonus["Owner"][wallet.id] = session.query(User).filter(
            User.id == wallet.owner
        ).one().username
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def orders_get(sql=""):
    q = session.query(Order)
    if not sql == "":
        q = session.query(Order).filter(text(sql))
    l = q.all()
    bonus = {
        'OrderedBy': {},
        'OrderedTo': {},
    }
    for order in l:
        bonus["OrderedBy"][order.id] = session.query(User).filter(
            User.id == order.orderedBy
        ).one().username
        bonus["OrderedTo"][order.id] = session.query(User).filter(
            User.id == order.orderedTo
        ).one().username
    return {
        "body": l,
        "query": q,
        "bonus": bonus
    }


def couponcodes_get(sql=""):
    if not sql == "":
        q = session.query(CouponCode).filter(text(sql))
    else:
        q = session.query(CouponCode)
    l = q.all()
    return {
        "body": l,
        "query": q
    }
