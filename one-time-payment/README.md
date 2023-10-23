# Checkout integration with stripe-hosted page for one time payment

Stripe allows for 2 types of recurring pricing model.
- [X] One time payment
- [ ] Recurring payment ([Example](https://github.com/Humairajahan/stripehub/tree/dev/custom-payment-flow))

## Source code
The source code for this is available on [Stripe's documentation](https://stripe.com/docs/checkout/quickstart)

## Project outline
Our codebase only contains the **backend** code required for integrating **one-time-payment** for your website on a **stripe-hosted page**. 

The following criterias have been met in this development:
- [ ] The pricing model has been made to be `one time payment`.
- [ ] Only admins have access to admin-specified resources.
- [ ] Admins can create multiple pricing models for the same product i.e. subscription package for a product can vary as per monthly or yearly.
- [ ] Admins can add discounts via coupons and promotion codes.
- [ ] The admin can only create pricing models for the currency `usd` only. If you want to allow support for more currencies in this application, please follow [this](https://stripe.com/docs/currencies?presentment-currency=IN)