LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := RemovePackages
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := AmbientSensePrebuilt AppDirectedSMSService arcore
LOCAL_OVERRIDES_PACKAGES += CarrierSetup ConnMO Ornament OPScreenRecord Snap ConnMetrics
LOCAL_OVERRIDES_PACKAGES += DCMO DevicePolicyPrebuilt DMService Drive
LOCAL_OVERRIDES_PACKAGES += GCS GoogleCamera
LOCAL_OVERRIDES_PACKAGES += MaestroPrebuilt Maps MyVerizonServices
LOCAL_OVERRIDES_PACKAGES += PixelLiveWallpaperPrebuilt NgaResources PrebuiltGmail Velvet
LOCAL_OVERRIDES_PACKAGES += RecorderPrebuilt ScribePrebuilt Recorder
LOCAL_OVERRIDES_PACKAGES += PixelLiveWallpaperPrebuilt SafetyHubPrebuilt WellbeingPrebuilt WellbeingPreBuilt
LOCAL_OVERRIDES_PACKAGES += SafetyHubPrebuilt SCONE ScribePrebuilt Showcase SoundAmplifierPrebuilt SprintDM SprintHM
LOCAL_OVERRIDES_PACKAGES += Tycho
LOCAL_OVERRIDES_PACKAGES += USCCDM
LOCAL_OVERRIDES_PACKAGES += Videos VZWAPNLib VzwOmaTrigger
LOCAL_OVERRIDES_PACKAGES += WallpapersBReel2020 obdm_stub
LOCAL_OVERRIDES_PACKAGES += YouTube YouTubeMusicPrebuilt
LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)
