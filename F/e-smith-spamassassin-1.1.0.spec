Summary: e-smith server and gateway - spamassassin anti-spam module
%define name e-smith-spamassassin
Name: %{name}
%define version 1.1.0
%define release 9
Version: %{version}
Release: %smerelease %{release}
Packager: %{_packager}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-spamassassin-1.1.0-02.mitel_patch
Patch1: e-smith-spamassassin-1.1.0-04.mitel_patch
Patch2: e-smith-spamassassin-1.1.0-05.mitel_patch
Patch3: e-smith-spamassassin-1.1.0-06.mitel_patch
Patch4: e-smith-spamassassin-1.1.0-07.mitel_patch
Patch5: e-smith-spamassassin-1.1.0-08.mitel_patch
Patch6: e-smith-spamassassin-1.1.0-SimplifyDotQmail.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: e-smith-email >= 4.13.0-38
Requires: spamassassin ucspi-tcp daemontools
Requires: e-smith-lib >= 1.13.1-90
Requires: e-smith-base >= 4.13.16
Requires: e-smith-qmail >= 1.9.0-09sme02
Requires: perl(Net::DNS) >= 0.34-1
Requires: razor-agents >= 2.61-1
Requires: DCC
Requires: pyzor
BuildArchitectures: noarch
BuildRequires: e-smith-devtools >= 1.11.0-12
AutoReqProv: no

%description
e-smith server and gateway software - spamassassin anti-spam module

%changelog
* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Fri Sep 23 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-08sme01]
- Simplify .qmail template fragment and add Requires header
  for recent e-smith-qmail since we need 00setup from it [SF: 1252336]

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [1.1.0-08]
- Prepare for change of default database location. [SF: 1216546]

* Tue May 31 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-07]
- Default spamassassin{RejectLevel}==0 [Gordon SF:1202399]

* Fri May 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-06]
- Another update from Gordon.
- Use condredirect (redirecting to $USERNAME-junkmail)
  instead of sortspam [SF:1200336]
- Provide template for .qmail-junkmail
- Remove db defaults for qmail{DeliveryType,DeliveryInstruction}.
  We don't want one delivery instruction, we want as many as the
  user has requested. Each instruction should be enabled/disabled
  on a global and per-user basis, as per SortSpam
- TODO: Simplify e-smithForward20 in e-smith-email

* Fri May 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-05]
- Really add the new files in last patch from Shad/Gordon.

* Thu May  5 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-04]
- Various contributions from Shad Lords and Gordon Rowell, as follows
- Add sortspam from Shad Lords' e-smith-spamassassin
- Add lots of config entries and local.cf templates, also from Shad
- Modified templates to match new config db names
- Add migrate fragments

* Wed Apr 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-03]
- Change Requires header to "razor-agents".

* Mon Mar 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-02]
- Update config for SpamAssassin 3.0.2

* Wed Feb  4 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-01]
- rolling to dev - 1.1.0

* Wed Feb  4 2004 Michael Soulier <msoulier@e-smith.com>
- [1.0.0-01]
- rolling to stable - 1.0.0

* Thu Aug 28 2003 Michael Soulier <msoulier@e-smith.com>
- [0.0.8-02]
- Added K* init symlinks to runlevels 0, 1 and 6. [msoulier 9761]

* Thu Jun 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.8-01]
- Enable spamd by default [gordonr 9183]
- Simplify spamassassin-update script [gordonr 9183]
- Resolve spamd/spamassassing directory confusion [gordonr 9183]
- Change spamd use home directory to /var/spool/spamd [gordonr 9183]
- Log as smelog user in /var/log/spamd [gordonr 9183]
- Update SPEC file with new genfilelist [gordonr 9183]

* Fri Jun 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-23]
- Add path to /service/spamd so restart works [gordonr 9095]

* Mon Jun  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-22]
- Put back skip_rbl_checks|0 default [gordonr 8952]

* Mon Jun  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-21]
- Generate the correct config lines, and make each fragment 
  valid perl [gordonr 8960]

* Mon Jun  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-20]
- Move spamassassin configuration parameters into main configdb
  as properties of the spamassassing service [gordonr 8960]

* Mon Jun  9 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-19]
- Change config to use RBLs by default. [charlieb 8952]

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-18]
- Use create-system-user to create spamd user. [charlieb 6033]

* Tue Apr 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-17]
- Removed %post call - already done in various events [gordonr 2600]

* Tue Apr 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-16]
- Changed spamd uid (1003 already taken) - [gordonr 8368]

* Mon Apr 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-15]
- Let useradd add the group in %pre. Don't fail %pre if the uid is not
  unique [gordonr 8368]

* Wed Apr  9 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-14]
- Replace serviceControl() calls with "svc-stop" or "svc -t" as required,
  so that messages don't leak to console when spamd is restarted.
  [charlieb 7883]

* Thu Apr  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-13]
- Removed dangling panel link [gordonr 7787]

* Wed Apr  2 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-12]
- Add default DeliveryInstruction andi DeliveryType default
  properties for qmail, so that "sortspam" is used for local delivery.
  Update e-smith-email "requires" version to suit. [charlieb 2600]
- Change Copyright header to License. [charlieb]

* Wed Apr  2 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-11]
- Remove panel code. Greg's panel code can now be found in
  e-smith-spamassassin-panel. [charlieb 7787]
- Split action into spamassassin config/restart and procmail
  configure sections. Latter is not yet liked into any
  actions. [charlieb 2600]
- Remove db initialization parts of action script - init done by
  'defaults' fragments. [charlieb 7526]
- Do stop/restart of 'spamd', not 'spamassassin'. [charlieb 2600]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.7-10]
- Change panel Spam Control -> Spam filtering [gordonr 2600]

* Fri Mar 28 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-09]
- Fix problem with sorting of sensitivity labels in panel [charlieb 7910]

* Tue Mar 25 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-08]
- Remove -c from run file which starts spamd - we don't want to try
  to create missing user config files. [charlieb 2600]
- Create user spamd and run spamd as that userid. [charlieb 2600]

* Mon Mar 17 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-07]
- Add conf.global and wbl.global default configuration data. [charlieb 2600]

* Fri Mar 14 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-06]
- Various fixes to spamassassin db initialization templates - mostly CVS
  repository issues. [charlieb 2600]

* Fri Mar 14 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-05]
- Add the panel link for the new panel. Configure spamd to be paranoid
  and to create no use config files. [charlieb 2600]

* Fri Mar 14 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-04]
- Remove Greg's full-featured spamassassin panel. Consult CVS if you want
  to resurrect any of the code. [charlieb 2600]

* Fri Mar 14 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-03]
- Fix the minimal FM panel so that it runs. [charlieb 2600]
- Fix compile problems in spamassassin-update script. [charlieb 2600]

* Fri Mar 14 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-02]
- Add starter en-us lexicon for FM version of the panel. [charlieb 2600]

* Fri Mar 14 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.7-01]
- Use new defaults directory structure to initialize db entries.
  Add minimal Fm web panel. Add spamassassin-update to email-update 
  and bootstrap-console-save events. [charlieb 2600]

* Tue Feb  4 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.6-01]
- Roll new source tarball after the merge [gordonr 2600]

* Tue Feb  4 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.5-04]
- Merged in Greg Zartman's <greg@leiinc.com> contrib

* Wed Jan 29 2003 Greg Zartman <greg@leiinc.com>
- Fixed a small typo in spamassassin server-manager
  panel that caused a menu label to not show correctly

* Wed Jan 29 2003 Greg Zartman <greg@leiinc.com>
- [0.0.1-1]
- initial Alpha release

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.5-03]
- And rename /service/spamd as well [gordonr 2600]

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.5-02]
- Renamed spamassassin -> spamd to avoid conflict with spamassassin's
  init script [gordonr 2600]

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.5-01]
- Removed stray /etc/tcprules directory [gordonr 2600]

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.4-01]
- Deleted some detritus [gordonr 2600]

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.3-01]
- And an -as-source run to build the initial version [gordonr 2600]

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.2-02]
- Missed some files on initial import [gordonr 2600]

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.2-01]
- Initial import to 0.0.2

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-02]
- Initial SRPM from CVS [gordonr 2600]

* Sun Dec 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-1]
- Initial

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
perl createlinks

mkdir -p root/service
ln -s /var/service/spamd root/service/spamd

mkdir -p root/var/service/spamd/supervise
touch root/var/service/spamd/down

mkdir -p root/var/service/spamd/log/supervise

mkdir -p root/var/log/spamd

mkdir -p root/var/service/spamd/env

mkdir -p root/var/spool/spamd

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/spamd 'attr(01755,root,root)' \
    --file /var/service/spamd/down 'attr(0644,root,root)' \
    --file /var/service/spamd/run 'attr(0755,root,root)' \
    --dir /var/service/spamd/log 'attr(0755,root,root)' \
    --dir /var/service/spamd/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/spamd/supervise 'attr(0700,root,root)' \
    --file /var/service/spamd/log/run 'attr(0755,root,root)' \
    --dir /var/log/spamd 'attr(2750,smelog,smelog)' \
    --dir /var/spool/spamd 'attr(2750,spamd,spamd)' \
    > %{name}-%{version}-%{release}-filelist

%pre
/sbin/e-smith/create-system-user spamd 1005 \
    'spamassassin daemon user' /var/spool/spamd /bin/false

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
