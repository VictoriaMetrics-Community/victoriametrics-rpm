%define release_arch amd64
%ifarch aarch64
%define release_arch arm64
%endif

Name:    vmsingle
Version: 1.102.0
Release: 2
Summary: The best long-term remote storage for Prometheus

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v%{version}/victoria-metrics-linux-%{release_arch}-v%{version}.tar.gz

Source0: %{name}.service
Source1: vmsingle.conf
Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/echo, /usr/bin/chown
Requires(postun): /usr/sbin/userdel
BuildRequires: curl

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)

%if %{use_systemd}
Requires: systemd
BuildRequires: systemd
%endif

%description
VictoriaMetrics - the best long-term remote storage for Prometheus

%prep
curl -L %{url} > victoria-metrics.tar.gz
tar -zxf victoria-metrics.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 -d %{buildroot}/etc/victoriametrics/single
cp %{SOURCE1} %{buildroot}/etc/victoriametrics/single
cp victoria-metrics-prod %{buildroot}%{_bindir}/victoria-metrics-prod
%{__install} -m 0755 -d %{buildroot}/var/lib/victoria-metrics-data
%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} \
    %{buildroot}%{_unitdir}/%{name}.service
%endif

%pre
/usr/bin/getent group victoriametrics > /dev/null || /usr/sbin/groupadd -r victoriametrics
/usr/bin/getent passwd victoriametrics > /dev/null || /usr/sbin/useradd -r -d /var/lib/victoria-metrics-data -s /bin/bash -g victoriametrics victoriametrics
%{__mkdir} -p /var/lib/victoria-metrics-data
/usr/bin/echo "WARINING: chown -R victoriametrics:victoriametrics /var/lib/victoria-metrics-data"
/usr/bin/echo "THIS MAY TAKE SOME TIME"
/usr/bin/chown -R victoriametrics:victoriametrics /var/lib/victoria-metrics-data

%post
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%preun
%if %use_systemd
/usr/bin/systemctl stop %{name}
%endif

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%files
%config /etc/victoriametrics/single/vmsingle.conf
%{_bindir}/victoria-metrics-prod
%dir %attr(0775, victoriametrics, victoriametrics) /var/lib/victoria-metrics-data
%if %{use_systemd}
%{_unitdir}/%{name}.service
%endif
