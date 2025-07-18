%define release_arch amd64
%ifarch aarch64
%define release_arch arm64
%endif

Name:    vmselect
Version: 1.121.0
Release: 1
Summary:  accepts the ingested data and spreads it among vmselect nodes according to consistent hashing over metric name and all its labels

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v%{version}/victoria-metrics-linux-%{release_arch}-v%{version}-cluster.tar.gz

Source0: %{name}.service
Source1: %{name}.conf

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
vmselect accepts the ingested data and spreads it among vmselect nodes according to consistent hashing over metric name and all its labels

%prep
curl -L %{url} > victoria-metrics-%{release_arch}-cluster.tar.gz
tar -zxf victoria-metrics-%{release_arch}-cluster.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 -d %{buildroot}/etc/victoriametrics/vmcluster
cp %{SOURCE1} %{buildroot}/etc/victoriametrics/vmcluster/
%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} %{buildroot}%{_unitdir}/%{name}.service
%endif
cp vmselect-prod %{buildroot}%{_bindir}/vmselect-prod

%pre
/usr/bin/getent group victoriametrics > /dev/null || /usr/sbin/groupadd -r victoriametrics
/usr/bin/getent passwd victoriametrics > /dev/null || /usr/sbin/useradd -r -m -d /home/victoriametrics -s /bin/bash -g victoriametrics victoriametrics

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
%{_bindir}/vmselect-prod
%dir %attr(0775, victoriametrics, victoriametrics) /etc/victoriametrics/vmcluster
%config /etc/victoriametrics/vmcluster/vmselect.conf
%if %{use_systemd}
%{_unitdir}/vmselect.service
%endif
