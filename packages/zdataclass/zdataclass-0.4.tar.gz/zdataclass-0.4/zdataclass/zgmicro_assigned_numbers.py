from zdataclass.zdataclass import *

class profile_roles(IntEnum8):
    Role_BAP_Unicast_Server     = 1
    Role_BAP_Unicast_Client     = 2
    Role_BAP_Broadcast_Source   = 3
    Role_BAP_Broadcast_Sink     = 4
    Role_BAP_Scan_Delegator     = 5
    Role_BAP_Broadcast_Assistant= 6
    Role_VCP_Renderer           = 7
    Role_VCP_Controller         = 8
    Role_MCP_Server             = 9
    Role_MCP_Client             = 10  
    Role_GAT_Server             = 11
    Role_GAT_Client             = 12
    Role_CSIP_Member            = 13
    Role_CSIP_Coordinator       = 14
    Role_CCP_Client             = 15
    Role_A2DP_Sink              = 24
    Role_A2DP_Source            = 25
    Role_AVRCP_Target           = 26
    Role_AVRCP_Controller       = 27
    Role_HFP_HF                 = 28
    Role_HFP_AG                 = 29


BM_GAT_Server_Roles = ((1 <<profile_roles.Role_GAT_Server) |\
                                 (1 <<profile_roles.Role_BAP_Unicast_Server) |\
                                 (1 <<profile_roles.Role_VCP_Renderer) |\
                                 (1 <<profile_roles.Role_MCP_Server) |\
                                 (1 <<profile_roles.Role_CSIP_Member) |\
                                 (1 <<profile_roles.Role_BAP_Scan_Delegator))
                                 
BM_GAT_Client_Roles = ((1 <<profile_roles.Role_GAT_Client) |\
                                     (1 <<profile_roles.Role_BAP_Unicast_Client) |\
                                     (1 <<profile_roles.Role_VCP_Controller) |\
                                     (1 <<profile_roles.Role_MCP_Client))

class VAPP_Scenarios(IntEnum8):
    APP_SCENARIO_SOUNDBAR             = 0
    APP_SCENARIO_SOUNDBAR_HEADSET     = 1
    APP_SCENARIO_SUBWOOFER            = 2
    APP_SCENARIO_WIRELESS_USB_DONGLE  = 3
    APP_SCENARIO_WIRELESS_USB_HEADSET = 4
    APP_SCENARIO_ABIS                 = 5
    APP_SCENARIO_WMIC_SINK            = 6
    APP_SCENARIO_WMIC_SOURCE          = 7
    APP_SCENARIO_MCSB_TX              = 8
    APP_SCENARIO_MCSB_RXL             = 9
    APP_SCENARIO_MCSB_RXR             = 10
    APP_SCENARIO_MCSB_RXS             = 11
    APP_SCENARIO_SHAREME              = 12
    APP_SCENARIO_PROFILE_TEST         = 13
    APP_SCENARIO_BQB_TEST             = 20
    APP_SCENARIO_KARAOKE              = 21
    APP_SCENARIO_TOP                  = 255


