from . import db
from .models import Bill, SubBill
from sqlalchemy import and_

def create_bill_object(total,sub_bills):
    bill = Bill(total=total)
    for sub_bill in sub_bills:
        sub_bill_obj = SubBill(amount=sub_bill["amount"], reference=sub_bill.get("reference"))
        bill.sub_bills.append(sub_bill_obj)

    db.session.add(bill)
    db.session.commit()
    return True

def get_filtered_bills(reference, total_from, total_to):
    # Building the query based on filters
    query = Bill.query.join(SubBill)

    if reference:
        reference=reference.lower()
        query = query.filter(SubBill.reference.ilike(f"%{reference}%"))

    if total_from and total_to:
        query = query.filter(and_(Bill.total >= total_from, Bill.total <= total_to))


    # Executing the query
    bills = query.all()

    # Converting the results to a list of mappings
    result = []
    for bill in bills:
        result.append({
            "id": bill.id,
            "total": bill.total,
            "sub_bills": [
                {
                    "id": sub_bill.id,
                    "amount": sub_bill.amount,
                    "reference": sub_bill.reference
                }
                for sub_bill in bill.sub_bills
            ]
        })
    return result
