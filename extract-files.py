#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove_arch_suffix,
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_clang_rt_ubsan,
    libs_proto_3_9_1,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/chime',
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sm8250',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/display',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'hardware/xiaomi',
]

lib_fixups: lib_fixups_user_type = {
    libs_proto_3_9_1: lib_fixup_vendorcompat,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/seccomp_policy/vendor.qti.hardware.dsp.policy': blob_fixup()
        .add_line_if_missing('madvise: 1'),
    'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing('ettid: 1'),
    'vendor/lib64/camera/components/com.qti.node.mialgocontrol.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    ('vendor/lib64/mediadrm/libwvdrmengine.so',
     'vendor/lib64/libwvhidl.so',
     'vendor/lib/mediadrm/libwvdrmengine.so',): blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so'),
    'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
        .sig_replace('13 0A 00 94', '1F 20 03 D5'),
    'vendor/lib64/libdpmqmihal.so': blob_fixup()
        .replace_needed('com.qualcomm.qti.dpm.api@1.0.so', 'com.qualcomm.qti.dpm.api@1.0_vendor.so'),
    'vendor/bin/dpmQmiMgr': blob_fixup()
        .replace_needed('com.qualcomm.qti.dpm.api@1.0.so', 'com.qualcomm.qti.dpm.api@1.0_vendor.so'),
    'vendor/lib64/hw/vendor.qti.hardware.fm@1.0-impl.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.fm@1.0.so', 'vendor.qti.hardware.fm@1.0_vendor.so'),
    'vendor/bin/hw/android.hardware.bluetooth@1.0-service-qti': blob_fixup()
        .replace_needed('vendor.qti.hardware.fm@1.0.so', 'vendor.qti.hardware.fm@1.0_vendor.so'),
    'system_ext/lib64/lib-imsvt.so': blob_fixup()
        .replace_needed('vendor.qti.imsrtpservice@3.0.so', 'vendor.qti.imsrtpservice@3.0_system_ext.so'),
    'vendor/lib64/hw/gf_fingerprint.default.so': blob_fixup()
        .fix_soname(),
    'vendor/lib64/hw/focal_fingerprint.default.so': blob_fixup()
        .fix_soname(),
    ('vendor/bin/STFlashTool',
     'vendor/lib64/libstfactory-vendor.so',): blob_fixup()
        .add_needed('libbase_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'chime',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
