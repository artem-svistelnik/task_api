from flask import request, jsonify
from my_app.models import Products, Reviews
from my_app import app, db, cache


@app.route('/product/<product_id>/', methods=['GET'])
@app.route('/product/<product_id>/<int:page>/', methods=['GET'])
@app.route('/product/<product_id>/<int:page>/<int:per_page>/', methods=['GET'])
@cache.cached(timeout=10)
def get_products(product_id, page=1, per_page=1):
    product_data = Products.query.filter_by(id=product_id).first_or_404()
    product_reviews = Reviews.query.filter_by(
        products_asin=product_data.asin).paginate(page, per_page, True).items
    for p in range(len(product_reviews)):
        product_reviews[p] = product_reviews[p].to_dict()
    return jsonify(product_data.to_dict(), product_reviews)


@app.route('/put_review/<product_id>/', methods=['PUT'])
def put_review(product_id):
    product = Products.query.filter_by(id=product_id).first_or_404()
    new_review = Reviews(products_asin=product.asin,
                         title=request.json['title'],
                         review=request.json['review'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 200


if __name__ == '__main__':
    app.run()
