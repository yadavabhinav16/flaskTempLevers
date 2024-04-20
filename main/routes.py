from . import app
from flask import Flask, render_template, request, url_for, redirect, jsonify
from .models import Bill, SubBill
from sqlalchemy import or_,and_
from .database import create_bill_object, get_filtered_bills


@app.route('/hello')
def hello():
    return 'Hello, Levers!'

@app.route("/bills", methods=["POST"])
def create_bill():
    # Get query parameters from the request JSON
    data = request.get_json()
    total = data.get("total")
    sub_bills = data.get("sub_bills")

    ret = "Bill created successfully" if create_bill_object(total, sub_bills) else "Unable to create bill"

    return jsonify({"message": ret})


@app.route("/bills", methods=["GET"])
def get_bills():
    # Get query parameters from the request
    reference = request.args.get("reference", None)
    total_from = request.args.get("total_from", type=float, default=None)
    total_to = request.args.get("total_to", type=float, default=None)

    result = get_filtered_bills(reference, total_from, total_to)

    return jsonify(result)
