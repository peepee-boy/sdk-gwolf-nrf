/*
 * Copyright (c) 2019 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
 */

#include "gpio_pins.h"

/* This configuration file is included only once from button module and holds
 * information about pins forming keyboard matrix.
 */

/* This structure enforces the header file is included only once in the build.
 * Violating this requirement triggers a multiple definition error at link time.
 */
const struct {} buttons_def_include_once;

static const struct gpio_pin col[] = {};

static const struct gpio_pin row[] = {
	{ .port = 0, .pin = 2 },
	{ .port = 1, .pin = 14 },
	{ .port = 1, .pin = 15 },
	{ .port = 0, .pin = 29 },
	{ .port = 0, .pin = 31 },
	{ .port = 0, .pin = 24 },
	{ .port = 0, .pin = 22 },
	{ .port = 0, .pin = 4 },
};
