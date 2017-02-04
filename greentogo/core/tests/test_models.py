def test_location_has_uuid(checkin_location):
    assert checkin_location.uuid is not None


def test_subscription_has_admin(subscription1):
    assert subscription1.admin is not None


def test_available_boxes_for_subscription(subscription2):
    assert subscription2.available_boxes() == 2


def test_available_boxes_after_checkout(subscription2, checkout_location):
    subscription2.tag_location(checkout_location)
    assert subscription2.available_boxes() == 1


def test_available_boxes_after_multiple_tags(subscription2, checkin_location,
                                             checkout_location):
    subscription2.tag_location(checkout_location)
    subscription2.tag_location(checkout_location)
    subscription2.tag_location(checkin_location)
    subscription2.tag_location(checkout_location)
    subscription2.tag_location(checkin_location)
    subscription2.tag_location(checkin_location)
    subscription2.tag_location(checkout_location)
    assert subscription2.available_boxes() == 1


def test_subscription_can_checkout(subscription1, checkout_location):
    assert subscription1.can_checkout()
    subscription1.tag_location(checkout_location)
    assert not subscription1.can_checkout()