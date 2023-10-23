# Checkout integration with a custom payment flow for a recurring pricing model

**Stripe** supports 3 types of payment integration. 
- [ ] Checkout with Stripe-hosted page 
- [ ] Checkout with embedded form 
- [X] Checkout with a custom payment flow

While implementation of the first 2 requires a `low-code integration` (you only need to create checkout sessions and read updates on them in the backend while stripe handles the rest), the third option lets us explore further into the customization of the payment flow. Here, we are going to implement this one.

## Source code
The source code for this is available on Stripe's documentation.
1. [Quickstart](https://stripe.com/docs/payments/quickstart)
2. [Text-based guide](https://stripe.com/docs/payments/accept-a-payment?ui=elements)

You can implement the full-stack application with Stripe's **integration builder** which you may find on their quickstart page by clicking on the `Download full app`.

## Project outline

Our codebase only contains the backend code required for integrating a custom payment flow with your website or application. 

The following criterias have been met in this development:

### `Product and pricing model`

- [ ] Only admins have the access to create products and pricing models.
- [X] Admins can create multiple pricing models for the same product i.e. the subscription package for a product can vary as per monthly or yearly. 
- [X] The pricing model has been made `recurring`.
- [X] The admin can only create pricing models for the following currencies: `usd`, `eur` and `inr`. If you want to allow support for more currencies in this application, please follow [this](https://stripe.com/docs/currencies?presentment-currency=IN).
