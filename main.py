import pickle
import streamlit as st
from helper import map_region
import pandas as pd

filename = 'Model_RF.pkl'
model = pickle.load(open(filename, 'rb'))


def main():
    st.title('Churn Prediction - Brazilian Olist')

    # Customer State
    # customerState = st.text_input('Customer State')
    # # Order Payment Gap
    # orderPaymentGap = st.number_input('Order Payment Gap (in minutes)')
    # st.write('(Order Approved Date - Order Purchase Date), if there is more then 1 order, please input the median order payment gap')
    # # Delivery Delay
    # deliveryDelay = st.number_input('Delivery Delay (in hours)')
    # st.write('Order Delivered Date - Order Estimated Delivery Date, if there is more then 1 order, please input the median delivery delay')
    # # Order
    # orderCount = st.number_input('Order Count')
    # # Active Order
    # options = ['Yes', 'No']
    # activeOrder = st.radio("Active Order", options, captions=[
    #     'if all order_status is not shipped, processing, approved, or invoiced',
    #     'if all order_status is shipped, processing, approved, or invoiced'
    # ])
    # # Review Score
    # reviewScore = st.number_input('Review Score')
    # st.write(
    #     'if there is more then 1 review score, please input the median review score')
    # # Price
    # price = st.number_input('Price')
    # st.write('if there is more then 1 price, please input the median price')
    # # Freight Value
    # freightValue = st.number_input('Freight Value')
    # st.write(
    #     'if there is more then 1 freight value, please input the median freight value')
    # # Payment Sequential
    # paymentSequential = st.number_input('Payment Sequential')
    # st.write(
    #     'if there is more then 1 payment sequential, please input the median payment sequential')
    # # Payment Value
    # paymentValue = st.number_input('Payment Value')
    # st.write(
    #     'if there is more then 1 payment value, please input the median payment value')
    # # Payment Type Count
    # paymentTypeCount = st.number_input('Payment Type Count')
    # st.write('Total payment type')
    # # Order Qty
    # orderQty = st.number_input('Item Quantity')
    # st.write('Total item quantity from the order, if there is more then 1 order, please input the median item qty')
    # # Product Category N
    # productCategoryN = st.number_input('Product Unique Category Count')
    # st.write('Total unique product category')
    # # Product Volume CM3
    # productVolumeCM3 = st.number_input('Product Volume')
    # st.write('if there is more then 1 product, please input the median product volume')
    # # Product Weight G
    # productWeightG = st.number_input('Product Weight(g)')
    # st.write(
    #     'if there is more then 1 product, please input the median product weight(g)')
    # # Product Name Length
    # productNameLength = st.number_input('Product Name Length')
    # st.write(
    #     'if there is more then 1 product, please input the median product name length')
    # # Product Description Length
    # productDescriptionLength = st.number_input('Product Description Length')
    # st.write(
    #     'if there is more then 1 product, please input the median product description length')
    # # Product Photos Qty
    # productPhotosQty = st.number_input('Product Photos Quantity')
    # st.write(
    #     'if there is more then 1 product, please input the median product photos quantity')

    # # Prediction Code
    # if st.button('Predict'):
    #     customer_region = map_region(customerState)
    #     list_features = ['order_payment_gap_mnt', 'delivery_delay_hr', 'order', 'active_order', 'review_score', 'price', 'freight_value', 'payment_sequential', 'payment_value', 'payment_type_count',
    #                      'order_qty', 'product_category_n', 'product_volume_cm3', 'product_weight_g', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'customer_region']
    #     if activeOrder == 'Yes':
    #         valueActiveOrder = 1
    #     else:
    #         valueActiveOrder = 0
    #     input_data = pd.DataFrame(
    #         [[orderPaymentGap, deliveryDelay, orderCount, valueActiveOrder, reviewScore, price, freightValue, paymentSequential, paymentValue,
    #             paymentTypeCount, orderQty, productCategoryN, productVolumeCM3, productWeightG, productNameLength, productDescriptionLength, productPhotosQty, customer_region]],
    #         columns=list_features
    #     )
    #     makePrediction = model.predict(input_data)
    #     output = makePrediction[0]
    #     st.success('The customer is churn' if output ==
    #                1 else 'The customer is not churn')


if __name__ == '__main__':
    main()
