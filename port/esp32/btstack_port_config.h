//
// btstack_config.h for esp32 port
//
// Documentation: https://bluekitchen-gmbh.com/btstack/#how_to/
//

#ifndef BTSTACK_PORT_CONFIG_H
#define BTSTACK_PORT_CONFIG_H

#include "esp_bt.h"

// Port related features
#define HAVE_ASSERT
#define HAVE_BTSTACK_STDIN
#define HAVE_EMBEDDED_TIME_MS
#define HAVE_FREERTOS_INCLUDE_PREFIX
#define HAVE_FREERTOS_TASK_NOTIFICATIONS
#define HAVE_MALLOC

// HCI Controller to Host Flow Control
#define ENABLE_HCI_CONTROLLER_TO_HOST_FLOW_CONTROL

void btstack_esp32_register_configuration_customizer(void (*congiguration_customizer)(esp_bt_controller_config_t *cfg));

#endif
