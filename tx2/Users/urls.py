from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
                         
    # USER REGISTRATION , LOGIN AND RELATED STUFF
        #INDEX PAGES
        url(r'^login/$','Users.Views.UserViews.Login_index'),
        url(r'^logout/$','Users.Views.UserViews.log_out'),
        url(r'^register/$','Users.Views.UserViews.CreateUserIndex'),
        url(r'^password/change/$','Users.Views.UserViews.ChangePassIndex'),
        url(r'^password/change/change/$','Users.Views.UserViews.ChangePass'),
        url(r'^password/reset/$','Users.Views.UserViews.ResetPasswordIndex'),
        url(r'^password/reset/reset/$','Users.Views.UserViews.ResetPass'),
        # post-back for logging in 
        url(r'^login/log_in/$','Users.Views.UserViews.log_in'),
        url(r'^dashboard/$','Users.Views.UserViews.view_dashboard'),
        url(r'^register/new/$','Users.Views.UserViews.CreateUserFromSite'),
        url(r'^authenticate/email/(?P<token>\S+)/(?P<refs>\d+)/$','Users.Views.UserViews.AuthenticateUserFromEmail'),
        
        url(r'^admin/$','Users.Views.UserAdminViews.ListAllUsers'),
        url(r'^admin/(?P<userid>\d+)/edit/$','Users.Views.UserAdminViews.EditUserIndex'),
        url(r'^admin/(?P<userid>\d+)/edit/edit/$','Users.Views.UserAdminViews.EditUser'),
    ###########################################################################################
   url(r'^grouptype/$','Users.Views.GroupTypeViews.GroupTypeIndex'),
   url(r'^grouptype/create/$','Users.Views.GroupTypeViews.GroupTypeIndex'),
   url(r'^grouptype/create/new/$','Users.Views.GroupTypeViews.CreateNewGroup'), 
   
   url(r'^group/$','Users.Views.GroupViews.GroupIndex',{'__list':'true','__create':'false'}),
   url(r'^group/create/$','Users.Views.GroupViews.GroupIndex',{'__list':'false','__create':'true'}),
   url(r'^group/create/new/$','Users.Views.GroupViews.CreateNewGroup'), 
 #   url(r'^group/(?P<gid>\d+)/users/add/$','txUser.Views_Group.AddUsers_Index'),
  #  url(r'^group/(?P<gid>\d+)/users/add/new/$','txUser.Views_Group.AddUsersToGroup'),
  #  url(r'^group/(?P<gid>\d+)/users/edit/$','txUser.Views_Group.EditUsers_Index'),

    
    # admin
   # url(r'^admin/$','txUser.UserViews.ListUsers'),
)               
