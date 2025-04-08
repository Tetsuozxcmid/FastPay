const createCheckoutSession = function(priceId) {
    return fetch("/create-order", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            priceId: priceId
        })

    }).then(function(result) {
        return result.json();
    });
};


document.addEventListener("DOMContentLoaded", function(event) {

    fetch("/api/stripe-config")

    .then(function(response) {
        return response.json();
    })

    .then(function(data) {

        const stripePublicKey = data.stripePublicKey;
        const premiumPriceId = data.premiumPriceId;
        const basicPriceId = data.basicPriceId;
        const stripe = Stripe(stripePublicKey);

        document
            .getElementById("checkout-premium")
            .addEventListener("click", function(evt) {
                createCheckoutSession(premiumPriceId)
                    .then(function(data) {
                        stripe.redirectToCheckout({ sessionId: data.session_id });
                    });
            });

        document
            .getElementById("checkout-basic")
            .addEventListener("click", function(evt) {
                createCheckoutSession(basicPriceId)
                    .then(function(data) {
                        stripe.redirectToCheckout({ sessionId: data.session_id });
                    });
            });
    })



    .catch(function(error) {
        console.error("Ошибка загрузки конфигурации Stripe:", error);
    });
});